#!/usr/bin/env python3
"""Generate 800 student records for the school management system."""

import json
import random
from datetime import datetime, timedelta

# Indian names for realistic data
FIRST_NAMES = [
    'Aarav', 'Aditya', 'Arjun', 'Aryan', 'Ashok', 'Amar', 'Anant', 'Anish', 'Aniket', 'Ajay',
    'Akshay', 'Akshit', 'Apurv', 'Arnav', 'Arvind', 'Aseem', 'Atharv', 'Avanish', 'Avichal', 'Ayush',
    'Bhavesh', 'Bhavit', 'Bhavin', 'Brijesh', 'Bhupen', 'Bhupesh', 'Bharat', 'Bhaskar', 'Bikram', 'Bimal',
    'Chirag', 'Chitraj', 'Chirayu', 'Chetan', 'Chinmay', 'Chandra', 'Chandresh', 'Chavit', 'Chavi', 'Chavi',
    'Darshan', 'Darpan', 'Deepak', 'Deba', 'Deven', 'Devendra', 'Devin', 'Devraj', 'Devrath', 'Dharam',
    'Dheeraj', 'Dhruv', 'Dharma', 'Dinesh', 'Dinanath', 'Diptesh', 'Divesh', 'Diwakar', 'Dixit', 'Dorik',
    'Erat', 'Eswar', 'Eshwaran', 'Ethan', 'Evaan',
    'Fabio', 'Faisal', 'Farhan', 'Farjad', 'Farrahkhan', 'Farzin', 'Faizan', 'Fahmi', 'Fahad', 'Faraz',
    'Garnik', 'Gajendra', 'Gamit', 'Ganesh', 'Ganesha', 'Ganna', 'Gapshap', 'Gargesh', 'Garvit', 'Gaurav',
    'Girik', 'Girish', 'Gokul', 'Govind', 'Gopal', 'Goutam', 'Granth', 'Gravish', 'Grisham', 'Grover',
    'Hail', 'Hailey', 'Halim', 'Hamara', 'Hamid', 'Hamish', 'Hans', 'Hardik', 'Hari', 'Harish',
    'Harkesh', 'Harleen', 'Harman', 'Harmeet', 'Harmon', 'Harpreet', 'Harsha', 'Harsh', 'Harshad', 'Harshil',
    'Harshita', 'Hasim', 'Hasnain', 'Hassan', 'Hastin', 'Hatim', 'Hayden', 'Hayyan', 'Hemed', 'Hemendra',
    'Hemer', 'Hemraj', 'Hemsh', 'Hendre', 'Henrika', 'Hensil', 'Hercules', 'Herman', 'Hermen', 'Hermit',
    'Hersh', 'Hilmar', 'Himachal', 'Himalaya', 'Himani', 'Himansh', 'Himanshu', 'Himmat', 'Himnish', 'Hiranya',
    'Hiranu', 'Hiryan', 'Hiten', 'Hither', 'Hitesh', 'Hitik', 'Hobert', 'Hoda', 'Hodan', 'Hodgson',
    'Ishaaq', 'Ishanth', 'Ishant', 'Ishanvi', 'Ishanvid', 'Ishaq', 'Isharth', 'Isharya', 'Ishav', 'Ishayu',
    'Jagat', 'Jagdish', 'Jagendra', 'Jagesh', 'Jagit', 'Jagmohan', 'Jagnar', 'Jagnath', 'Jagran', 'Jagrat',
    'Jagric', 'Jagrip', 'Jagrit', 'Jagrup', 'Jagtej', 'Jagtid', 'Jagveer', 'Jagvir', 'Jagwant', 'Jahaan',
    'Kaabil', 'Kabali', 'Kabhid', 'Kabi', 'Kabin', 'Kabil', 'Kabir', 'Kabita', 'Kachru', 'Kadian',
    'Kailash', 'Kairav', 'Kairy', 'Kairya', 'Kaishav', 'Kaisle', 'Kaiyan', 'Kaji', 'Kaka', 'Kakar',
    'Laksh', 'Lakshan', 'Lakshay', 'Lakshit', 'Lakshmi', 'Lakshta', 'Lakshya', 'Laksmeet', 'Lakumen', 'Lakyan',
    'Lal', 'Laleet', 'Lalind', 'Lalirand', 'Lalitendra', 'Lalitesh', 'Laliteshwar', 'Lalith', 'Lalitary', 'Lalitesh',
    'Madhav', 'Madhavan', 'Madhav', 'Madhubhan', 'Madhukar', 'Madhuran', 'Madhusudan', 'Madhusudhan', 'Madura', 'Madhur',
    'Madhvendra', 'Madhvi', 'Madhvin', 'Madhvish', 'Madiha', 'Madihah', 'Madina', 'Madinah', 'Madini', 'Madith',
    'Naveen', 'Naveena', 'Navendra', 'Navern', 'Navesh', 'Navesha', 'Naveshwar', 'Navesh', 'Navi', 'Naviav',
    'Navid', 'Navidi', 'Navik', 'Naviksh', 'Navil', 'Navilesh', 'Navil', 'Navimandal', 'Navina', 'Navinash',
    'Omkar', 'Omkara', 'Ombir', 'Omesh', 'Omeshwar', 'Omid', 'Omkar', 'Omkarananda', 'Omkaranth', 'Omkarath',
    'Omkari', 'Omkaris', 'Ompat', 'Omraj', 'Omram', 'Omrishi', 'Omvir', 'Onaj', 'Ondra', 'Onesime',
    'Pranav', 'Pranavendra', 'Pranavi', 'Pranavya', 'Pranay', 'Pranaya', 'Pranayan', 'Pranbir', 'Pranchal', 'Prandip',
    'Prandishen', 'Praneeth', 'Pranesh', 'Praneshwar', 'Prangi', 'Prangy', 'Pranish', 'Pranit', 'Pranith', 'Pranjar',
    'Rajendra', 'Rajesh', 'Rajeshwar', 'Rajesh', 'Rajesh', 'Rajeswari', 'Rajeswaran', 'Rajeya', 'Rajib', 'Rajibh',
    'Rajil', 'Rajila', 'Rajilash', 'Rajilithi', 'Rajim', 'Rajimd', 'Rajimdev', 'Rajimdesh', 'Rajinder', 'Rajini',
    'Sachin', 'Sachinesh', 'Sachira', 'Sachiraj', 'Sachis', 'Sachish', 'Sachit', 'Sachitananda', 'Sachitva', 'Sachiva',
    'Sachiya', 'Sachman', 'Sachmandra', 'Sachman', 'Sachpratap', 'Sachraj', 'Sachveer', 'Sachvinder', 'Sad', 'Sadeep',
    'Sanjay', 'Sanjaya', 'Sanjeev', 'Sanjeeva', 'Sanjeet', 'Sanjit', 'Sanjith', 'Sanjiva', 'Sanjos', 'Sanjoib',
    'Sanjoy', 'Sanjya', 'Sankaradeva', 'Sankaramurthy', 'Sankaranarayana', 'Sankaranarayan', 'Sankara', 'Sankaranarayan',
    'Tarun', 'Taruna', 'Tarunesh', 'Tarunendu', 'Tarunendra', 'Tarunesh', 'Taruneshwar', 'Taruneshwara', 'Tarungi', 'Tarunika',
    'Taruniksha', 'Taruninder', 'Tarunish', 'Tarunita', 'Tarunja', 'Tarunjaya', 'Tarunjit', 'Tarunkamal', 'Tarunkannan', 'Tarunkaruna',
    'Uday', 'Udayan', 'Udayendra', 'Udayakirti', 'Udayakumar', 'Udayan', 'Udayan', 'Udayangra', 'Udayani', 'Udayanjali',
    'Udayanshu', 'Udayaprakash', 'Udayas', 'Udayashankara', 'Udayasheel', 'Udayashree', 'Udayat', 'Udayavinda', 'Udayveer', 'Udayvikrama',
    'Videv', 'Vidhaan', 'Vidhanchal', 'Vidhanka', 'Vidhansa', 'Vidhant', 'Vidharan', 'Vidharna', 'Vidharta', 'Vidhartesh',
    'Vidhasa', 'Vidhata', 'Vidhavendra', 'Vidhavan', 'Vidhavan', 'Vidhavendra', 'Vidhavindra', 'Vidhaya', 'Vidhayesh', 'Vidhayishtha',
    'Yash', 'Yasha', 'Yashas', 'Yashashvi', 'Yashashvin', 'Yashashvini', 'Yashshree', 'Yashasvi', 'Yashasvin', 'Yashasvinra',
    'Yashasya', 'Yashasya', 'Yashava', 'Yashava', 'Yashe', 'Yasheed', 'Yasheena', 'Yasheendra', 'Yasheer', 'Yasheesh',
    'Zain', 'Zainal', 'Zainally', 'Zainalabdin', 'Zainadine', 'Zainah', 'Zaino', 'Zainsuddin', 'Zaire', 'Zairene',
    'Zairul', 'Zais', 'Zaker', 'Zakeria', 'Zakeria', 'Zakera', 'Zakeri', 'Zakeya', 'Zakhar', 'Zakharia',
    'Ananya', 'Anya', 'Anika', 'Anisha', 'Anita', 'Anjali', 'Anjana', 'Anusha', 'Anushka', 'Anvita',
    'Arya', 'Asha', 'Ashika', 'Ashita', 'Ashna', 'Asmita', 'Ayana', 'Ayesha', 'Ayshita', 'Ayushi',
    'Bhavna', 'Bhavya', 'Bhumika', 'Bhupinder', 'Bhavini', 'Bhavisya', 'Bhawna', 'Bhavya', 'Bhavyata', 'Bhavyu',
    'Chiara', 'Chithi', 'Chitra', 'Chitrakshi', 'Chitra', 'Chitralekha', 'Chitrarekha', 'Chitrita', 'Chitriya', 'Chitrya',
    'Darshana', 'Darshani', 'Darshini', 'Darshnaa', 'Darshnavi', 'Darshneha', 'Darshnie', 'Darshnika', 'Darshvani', 'Darshvari',
    'Deepa', 'Deepali', 'Deepana', 'Deepani', 'Deepansha', 'Deepanshi', 'Deepanu', 'Deepara', 'Deepashi', 'Deepatha',
    'Disha', 'Dishita', 'Dishya', 'Divya', 'Divyaa', 'Divyan', 'Divyana', 'Divyani', 'Divyanka', 'Divyanse',
    'Esha', 'Eshita', 'Eshnaa', 'Eshna', 'Eshneha', 'Eshnita', 'Eshwari', 'Esita', 'Esna', 'Esra',
    'Fatima', 'Fatimah', 'Faria', 'Farida', 'Farina', 'Fariza', 'Farzana', 'Farzeen', 'Farzida', 'Fasihah',
    'Gaira', 'Gajra', 'Ganika', 'Ganiska', 'Ganya', 'Gara', 'Garbi', 'Gargi', 'Gari', 'Garima',
    'Garishi', 'Garitri', 'Garja', 'Garjana', 'Garji', 'Garmini', 'Garnika', 'Garonika', 'Garpini', 'Garsha',
    'Geeta', 'Geetakshi', 'Geetali', 'Geetana', 'Geetananda', 'Geetangi', 'Geetanjali', 'Geetanjuli', 'Geetansha', 'Geetanvi',
    'Gita', 'Gitakshi', 'Gital', 'Gitali', 'Gitamedha', 'Gitamrita', 'Gitananda', 'Gitangi', 'Gitanjali', 'Gitanja',
    'Gitta', 'Givangi', 'Giya', 'Giyata', 'Giyatri', 'Giyatrika', 'Giyatrita', 'Giyatya', 'Giyavati', 'Giyesha',
    'Gitika', 'Gitiksha', 'Gitima', 'Gitini', 'Gitipriya', 'Gitisha', 'Gitishka', 'Gitita', 'Gititha', 'Gitiya',
    'Gitu', 'Gituja', 'Gituki', 'Gitula', 'Gitumi', 'Gituna', 'Gitungi', 'Gitura', 'Gituta', 'Gituvi',
    'Hamsini', 'Hamsa', 'Hamsikha', 'Hamsila', 'Hamsini', 'Hamya', 'Hankita', 'Hanisha', 'Hanitha', 'Hankini',
    'Hansa', 'Hansaka', 'Hansakshar', 'Hansali', 'Hansana', 'Hansapriya', 'Hansashree', 'Hansata', 'Hansavati', 'Hansaveer',
    'Hasiya', 'Hasita', 'Hasitha', 'Hasna', 'Hasnaa', 'Hasnain', 'Hasna', 'Hasnida', 'Hasnika', 'Hasrin',
    'Havita', 'Havya', 'Haya', 'Hayari', 'Hayasha', 'Hayata', 'Hayati', 'Hayavati', 'Hayavati', 'Hayee',
    'Heena', 'Heena', 'Heenakshi', 'Heenali', 'Heenana', 'Heenaxi', 'Heesh', 'Heeta', 'Heithi', 'Heiti',
    'Heitra', 'Heituva', 'Heita', 'Heitu', 'Heitya', 'Heitra', 'Hejarati', 'Hejati', 'Hejia', 'Hejibi',
    'Ishita', 'Ishana', 'Ishani', 'Ishanika', 'Ishanki', 'Ishanvi', 'Ishanvini', 'Ishara', 'Isharanka', 'Isharasi',
    'Isharika', 'Isharini', 'Isharita', 'Isharyati', 'Ishata', 'Ishatara', 'Ishatika', 'Ishati', 'Ishatiya', 'Ishatri',
    'Jagadamba', 'Jagadambi', 'Jagadavali', 'Jagadgita', 'Jagadhatri', 'Jagadi', 'Jagalakshmi', 'Jagamukti', 'Jagamuktr', 'Jagamukti',
    'Jagana', 'Jaganak', 'Jaganakshi', 'Jaganallika', 'Jaganandini', 'Jaganandita', 'Jaganangana', 'Jaganaramani', 'Jaganarani', 'Jaganarita',
    'Jyoti', 'Jyotika', 'Jyotikira', 'Jyotila', 'Jyotilatika', 'Jyotili', 'Jyotilika', 'Jyotilina', 'Jyotilita', 'Jyotira',
    'Jyotirakshe', 'Jyotipriya', 'Jyotirama', 'Jyotiramani', 'Jyotirakshi', 'Jyotirasmi', 'Jyotirekha', 'Jyotirmala', 'Jyotirmati', 'Jyotirmi',
    'Kaaveri', 'Kaavya', 'Kabita', 'Kaboli', 'Kabra', 'Kacie', 'Kaciria', 'Kacynti', 'Kadambari', 'Kadambini',
    'Kadan', 'Kadamba', 'Kadambini', 'Kadambi', 'Kadamka', 'Kadamkini', 'Kadamkira', 'Kadamli', 'Kadamlika', 'Kadamsa',
    'Kailasha', 'Kailashananda', 'Kailasharani', 'Kailasha', 'Kailasmati', 'Kailashika', 'Kailashini', 'Kailashita', 'Kailashmrita', 'Kailashnanda',
    'Kajali', 'Kajalika', 'Kajalima', 'Kajalini', 'Kajalita', 'Kajaliya', 'Kajalka', 'Kajalli', 'Kajalprabha', 'Kajalpriya',
    'Keka', 'Kekavi', 'Kekasini', 'Kelana', 'Kelani', 'Kelipa', 'Kelini', 'Kelita', 'Keliya', 'Kelka',
    'Lakshmi', 'Lakshmi', 'Lakshmika', 'Lakshmikant', 'Lakshmikanti', 'Lakshmi', 'Lakshmi', 'Lakshmi', 'Lakshmi', 'Lakshmi',
    'Lalita', 'Lalitakanya', 'Lalitaksha', 'Lalitakshe', 'Lalitachandra', 'Lalitachand', 'Lalitadevi', 'Lalitaditya', 'Lalitafi', 'Lalitahara',
    'Madhavi', 'Madhavika', 'Madhavila', 'Madhavini', 'Madhavishi', 'Madhavita', 'Madhaviya', 'Madhavka', 'Madhavli', 'Madhavpriya',
    'Madhula', 'Madhulai', 'Madhulakshi', 'Madhulala', 'Madhulanga', 'Madhulangai', 'Madhulani', 'Madhularani', 'Madhulasa', 'Madhulatha',
    'Mala', 'Malaa', 'Malabai', 'Malacha', 'Malachi', 'Malada', 'Maladevi', 'Maladitya', 'Maladitya', 'Malaha',
    'Malavati', 'Malavati', 'Malavatika', 'Malavativati', 'Malavica', 'Malavi', 'Malavika', 'Malavikakshi', 'Malavikakshi', 'Malavikakshya',
    'Mamata', 'Mamtaa', 'Mamtakshi', 'Mamtali', 'Mamtamaya', 'Mamtamoh', 'Mamtamohina', 'Mamtananda', 'Mamtanandini', 'Mamtanandita',
    'Manada', 'Manchili', 'Mandakini', 'Mandal', 'Mandala', 'Mandalabai', 'Mandalakshmi', 'Mandalakshya', 'Mandalatha', 'Mandalathika',
    'Manjari', 'Manjarika', 'Manjaripriya', 'Manjaripriyanka', 'Manjrishka', 'Manjusha', 'Manjushikara', 'Manjushila', 'Manjushimi', 'Manjushina',
    'Manisha', 'Manishakanta', 'Manishakara', 'Manishakari', 'Manishakha', 'Manishaksha', 'Manisharama', 'Manisharangi', 'Manisharasa', 'Manisharathi',
    'Manorama', 'Manoramala', 'Manoramama', 'Manorama', 'Manorama', 'Manorama', 'Manorama', 'Manorama', 'Manorama', 'Manorama',
    'Marita', 'Maritalaya', 'Maritala', 'Maritalika', 'Maritalina', 'Maritalita', 'Maritamaya', 'Maritamohana', 'Maritana', 'Maritananda',
    'Maya', 'Mayaa', 'Mayabati', 'Mayaberi', 'Mayachakra', 'Mayachanda', 'Mayachandana', 'Mayachandani', 'Mayachandika', 'Mayachandini',
    'Meena', 'Meenakara', 'Meenakari', 'Meenaksha', 'Meenakshi', 'Meenakshi', 'Meenakshi', 'Meenakshi', 'Meenakshi', 'Meenakshi',
    'Megha', 'Meghaa', 'Meghada', 'Meghadhi', 'Meghadota', 'Meghaduta', 'Meghadutika', 'Meghar', 'Mehgara', 'Megharani',
    'Mera', 'Merabai', 'Meradevi', 'Meradhanvi', 'Meradhanvika', 'Meradhanvini', 'Meradhanvita', 'Meradhanvya', 'Meradevi', 'Meradiksha',
    'Mira', 'Miraa', 'Mirabai', 'Mirabai', 'Mirabehn', 'Mirajyoti', 'Mirakavi', 'Mirakrit', 'Miralaksha', 'Miramali',
    'Misha', 'Mishaa', 'Mishakara', 'Mishakari', 'Mishaksha', 'Mishakshi', 'Mishari', 'Misharika', 'Misharini', 'Misharita',
    'Naina', 'Nainaa', 'Nainakanya', 'Nainakara', 'Nainakari', 'Nainaksha', 'Nainakshi', 'Nainakshyada', 'Nainakshyaka', 'Nainakshya',
    'Nalini', 'Nalinakara', 'Nalinakari', 'Nalinaksha', 'Nalinakshi', 'Nalinakshyada', 'Nalinakshyaka', 'Nalinakshya', 'Nalinakshya', 'Nalinakshy',
    'Namita', 'Namitaa', 'Namitakara', 'Namitakari', 'Namitaksha', 'Namitakshi', 'Namitakshy', 'Namitakshy', 'Namitakshya', 'Namitakshy',
    'Natalia', 'Natalya', 'Natasha', 'NataSha', 'Natashaa', 'Natasharanya', 'Natasharanya', 'Natasharanya', 'Natasharanya', 'Natasharanya',
    'Naveen', 'Naveena', 'Naveenakara', 'Naveenakari', 'Naveenaksha', 'Naveenakshi', 'Naveenakshya', 'Naveenakshya', 'Naveenakshya', 'Naveenakshya',
    'Navi', 'Navya', 'Navyakara', 'Navyakari', 'Navyaksha', 'Navyakshi', 'Navyakshya', 'Navyakshya', 'Navyakshya', 'Navyakshya',
    'Neelaksha', 'Neelakshi', 'Neelakshya', 'Neelakshya', 'Neelakshya', 'Neelakshya', 'Neelakshya', 'Neelakshya', 'Neelakshya', 'Neelakshya',
    'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani', 'Neelamani',
    'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali', 'Neelanjali',
    'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima', 'Neelima',
    'Nikita', 'Nikitaa', 'Nikitakara', 'Nikitakari', 'Nikitaksha', 'Nikitakshi', 'Nikitakshya', 'Nikitakshya', 'Nikitakshya', 'Nikitakshya',
    'Nisha', 'Nishaa', 'Nishakara', 'Nishakari', 'Nishaksha', 'Nishakshi', 'Nishakshya', 'Nishakshya', 'Nishakshya', 'Nishakshya',
    'Nishtha', 'Nishtakara', 'Nishtakari', 'Nishtaksha', 'Nishtakshi', 'Nishtakshya', 'Nishtakshya', 'Nishtakshya', 'Nishtakshya', 'Nishtakshya',
    'Nita', 'Nitaa', 'Nitakara', 'Nitakari', 'Nitaksha', 'Nitakshi', 'Nitakshya', 'Nitakshya', 'Nitakshya', 'Nitakshya',
    'Netra', 'Netraa', 'Netrakara', 'Netrakari', 'Netraksha', 'Netrakshi', 'Netrakshya', 'Netrakshya', 'Netrakshya', 'Netrakshya',
    'Oindrila', 'Oindrilaaa', 'Oindrila', 'Oindrila', 'Oindrila', 'Oindrila', 'Oindrila', 'Oindrila', 'Oindrila', 'Oindrila',
    'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini', 'Ojaswini',
    'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi', 'Pallavi',
    'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma', 'Paloma',
    'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali', 'Pancali',
    'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita', 'Pandita',
    'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha', 'Panisha',
    'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati', 'Pranati',
    'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima', 'Pratima',
    'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti', 'Pratiti',
    'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha', 'Preetha',
    'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka', 'Priyanka',
    'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata', 'Priyata',
    'Priya', 'Priya', 'Priya', 'Priya', 'Priya', 'Priya', 'Priya', 'Priya', 'Priya', 'Priya',
    'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha', 'Priyavyatha',
    'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika', 'Radhika',
    'Radha', 'Radha', 'Radha', 'Radha', 'Radha', 'Radha', 'Radha', 'Radha', 'Radha', 'Radha',
    'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari', 'Rajeshwari',
    'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita', 'Ranjita',
    'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi', 'Rashi',
    'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita', 'Rashmita',
    'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika', 'Rasika',
    'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita', 'Rasita',
    'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna', 'Ratna',
    'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara', 'Ratnakara',
    'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari', 'Ratnakari',
    'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali', 'Ratnamali',
    'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari', 'Ratnamanjari',
    'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya', 'Ratnamaya',
    'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya', 'Ratnapriya',
    'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree', 'Ratnashree',
    'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri', 'Ratnasri',
    'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi', 'Ratnavi',
    'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya', 'Ratnaya',
]

LAST_NAMES = [
    'Sharma', 'Singh', 'Gupta', 'Kumar', 'Patel', 'Desai', 'Verma', 'Reddy', 'Khan', 'Malhotra',
    'Iyer', 'Menon', 'Nair', 'Pillai', 'Rao', 'Bhat', 'Saha', 'Jain', 'Chopra', 'Batra',
    'Saxena', 'Pandey', 'Singh', 'Yadav', 'Mishra', 'Arora', 'Kapoor', 'Khanna', 'Bhatt', 'Shah',
    'Modi', 'Trivedi', 'Dwivedi', 'Tiwari', 'Upadhyay', 'Dubey', 'Tyagi', 'Kashyap', 'Banerjee', 'Roy',
    'Bose', 'Dutta', 'Sengupta', 'Lahiri', 'Mukherjee', 'Chatterjee', 'Mallik', 'Sinha', 'Gosh', 'Das',
    'Nath', 'Mitra', 'Ghosh', 'Mazumdar', 'Banerjee', 'Dasgupta', 'Mukerji', 'Sil', 'Chakraborty', 'Bannerjee'
]

GRADES = ['9', '10', '11', '12']
SECTIONS = ['A', 'B', 'C', 'D']
SUBJECTS = ['Science', 'Mathematics', 'English', 'History', 'Geography', 'Literature', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Arts', 'Music', 'Physical Education']
CITIES = [
    'Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Pune', 'Kolkata', 'Chennai', 'Chandigarh',
    'Ahmedabad', 'Surat', 'Jaipur', 'Lucknow', 'Bhopal', 'Nagpur', 'Indore', 'Coimbatore',
    'Kochi', 'Vishakhapatnam', 'Vadodara', 'Ghaziabad', 'Noida', 'Gurgaon', 'Thane', 'Navi Mumbai'
]
NOTES = [
    'Excellent academic performance.', 'Good participation in class activities.', 'Needs improvement in studies.',
    'Talented in sports.', 'Active in cultural programs.', 'Shy but intelligent student.', 'Very disciplined.',
    'Requires extra attention.', 'Science enthusiast.', 'Math wizard.', 'Art lover.', 'Debate champion.',
    'Deserving of scholarship.', 'Leadership qualities.', 'Needs motivation.', 'Very creative.',
]

def generate_student_records(count=800):
    """Generate student records with realistic data."""
    students = []
    used_emails = set()
    
    for i in range(1, count + 1):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        
        # Generate unique email
        base_email = f"{first_name.lower()}.{last_name.lower()}@school.edu"
        email = base_email
        counter = 1
        while email in used_emails:
            email = f"{first_name.lower()}.{last_name.lower()}{counter}@school.edu"
            counter += 1
        used_emails.add(email)
        
        grade = random.choice(GRADES)
        section = random.choice(SECTIONS)
        age = random.randint(14, 18)
        phone = f"+91-{random.randint(98000, 99999)}-{random.randint(10000, 99999)}"
        gpa = round(random.uniform(2.0, 4.0), 2)
        status = random.choices(['Active', 'Inactive'], weights=[95, 5])[0]
        
        # Joined date - random between 2021 and 2024
        years_back = random.randint(0, 3)
        joined_date = (datetime.now() - timedelta(days=365*years_back + random.randint(0, 365))).strftime('%Y-09-01')
        
        subject = random.choice(SUBJECTS)
        avatar = (first_name[0] + last_name[0]).upper()
        attendance = random.randint(65, 99)
        city = random.choice(CITIES)
        address = f"Sector {random.randint(1, 50)}, {city}"
        
        # Parent info
        parent_first = random.choice(FIRST_NAMES)
        parent_last = last_name  # Usually same as student
        parent_name = f"{parent_first} {parent_last}"
        parent_phone = f"+91-{random.randint(98000, 99999)}-{random.randint(10000, 99999)}"
        
        notes = random.choice(NOTES)
        
        student = {
            "id": i,
            "name": f"{first_name} {last_name}",
            "grade": f"{grade}-{section}",
            "age": age,
            "email": email,
            "phone": phone,
            "gpa": gpa,
            "status": status,
            "joined": joined_date,
            "subject": subject,
            "avatar": avatar,
            "attendance": attendance,
            "address": address,
            "parent": parent_name,
            "parentPhone": parent_phone,
            "notes": notes
        }
        
        students.append(student)
    
    return students

if __name__ == '__main__':
    # Load existing data
    with open('/home/atul/Documents/method/accounts.json', 'r') as f:
        data = json.load(f)
    
    # Generate 800 new students
    print("Generating 800 student records...")
    new_students = generate_student_records(800)
    
    # Add to existing students
    data['students'].extend(new_students)
    
    # Update accounts.json
    with open('/home/atul/Documents/method/accounts.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✓ Successfully added 800 students to accounts.json")
    print(f"✓ Total students now: {len(data['students'])}")
    print(f"✓ File saved: /home/atul/Documents/method/accounts.json")
