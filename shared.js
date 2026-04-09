// ── EduCore Shared Data & Navigation ────────────────────────────────────────

// Auth guard
function authGuard(requiredRole=null) {
  const user = JSON.parse(localStorage.getItem('edu_auth') || 'null');
  if (!user) { window.location.href = 'index.html'; return null; }
  if (requiredRole && user.role !== requiredRole && user.role !== 'Super Admin') {
    window.location.href = 'index.html';
    return null;
  }
  return user;
}

function getCurrentUser() {
  return JSON.parse(localStorage.getItem('edu_auth') || 'null');
}

function logout() {
  localStorage.removeItem('edu_auth');
  window.location.href = 'index.html';
}

// ── Default Students Data ─────────────────────────────────────────────────
const DEFAULT_STUDENTS = [
  { id:1,name:'Aarav Sharma',grade:'10-A',age:16,email:'aarav.s@school.edu',phone:'+91-98765-01001',gpa:3.8,status:'Active',joined:'2023-09-01',subject:'Science',avatar:'AS',attendance:95,address:'Sector 5, Delhi',parent:'Vikram Sharma',parentPhone:'+91-98765-91001',notes:'Excellent in Physics competitions.' },
  { id:2,name:'Ananya Gupta',grade:'11-B',age:17,email:'ananya.g@school.edu',phone:'+91-98765-02002',gpa:3.9,status:'Active',joined:'2022-09-01',subject:'Mathematics',avatar:'AG',attendance:98,address:'Bandra, Mumbai',parent:'Priyanka Gupta',parentPhone:'+91-98765-92002',notes:'Math Olympiad finalist 2023.' },
  { id:3,name:'Arjun Kumar',grade:'9-C',age:15,email:'arjun.k@school.edu',phone:'+91-98765-03003',gpa:3.5,status:'Active',joined:'2024-09-01',subject:'Arts',avatar:'AK',attendance:88,address:'Indiranagar, Bangalore',parent:'Ashok Kumar',parentPhone:'+91-98765-93003',notes:'Talented in visual arts and design.' },
  { id:4,name:'Anaya Patel',grade:'12-A',age:18,email:'anaya.p@school.edu',phone:'+91-98765-04004',gpa:4.0,status:'Active',joined:'2021-09-01',subject:'Literature',avatar:'AP',attendance:99,address:'Ahmedabad, Gujarat',parent:'Rajeev Patel',parentPhone:'+91-98765-94004',notes:'Valedictorian candidate, debate captain.' },
  { id:5,name:'Nikhil Singh',grade:'10-B',age:16,email:'nikhil.s@school.edu',phone:'+91-98765-05005',gpa:3.2,status:'Inactive',joined:'2023-09-01',subject:'History',avatar:'NS',attendance:72,address:'Sector 15, Noida',parent:'Neha Singh',parentPhone:'+91-98765-95005',notes:'Currently on medical leave.' },
  { id:6,name:'Priya Desai',grade:'11-A',age:17,email:'priya.d@school.edu',phone:'+91-98765-06006',gpa:3.7,status:'Active',joined:'2022-09-01',subject:'Chemistry',avatar:'PD',attendance:96,address:'Whitefield, Bangalore',parent:'Rajesh Desai',parentPhone:'+91-98765-96006',notes:'Science fair winner 2023.' },
  { id:7,name:'Jagrit Verma',grade:'9-A',age:15,email:'jagrit.v@school.edu',phone:'+91-98765-07007',gpa:3.0,status:'Active',joined:'2024-09-01',subject:'Physical Ed',avatar:'JV',attendance:91,address:'Dwarka, Delhi',parent:'Lata Verma',parentPhone:'+91-98765-97007',notes:'Captain of basketball team.' },
  { id:8,name:'Aisha Reddy',grade:'12-B',age:18,email:'aisha.r@school.edu',phone:'+91-98765-08008',gpa:3.95,status:'Active',joined:'2021-09-01',subject:'Biology',avatar:'AR',attendance:97,address:'Hyderabad, Telangana',parent:'Anil Reddy',parentPhone:'+91-98765-98008',notes:'Pre-med track, Harvard applicant.' },
  { id:9,name:'Farhan Khan',grade:'10-C',age:16,email:'farhan.k@school.edu',phone:'+91-98765-09009',gpa:3.4,status:'Active',joined:'2023-09-01',subject:'Computer Science',avatar:'FK',attendance:93,address:'Pune, Maharashtra',parent:'Lalit Khan',parentPhone:'+91-98765-99009',notes:'Built school mobile app.' },
  { id:10,name:'Zara Malhotra',grade:'11-C',age:17,email:'zara.m@school.edu',phone:'+91-98765-10010',gpa:3.6,status:'Active',joined:'2022-09-01',subject:'Music',avatar:'ZM',attendance:94,address:'Sector 8, Chandigarh',parent:'Mohan Malhotra',parentPhone:'+91-98765-910010',notes:'Lead violin, school orchestra.' },
];

const DEFAULT_TEACHERS = [
  { id:1,name:'Dr. Arun Kumar',subject:'Mathematics',grade:'10-12',email:'arun.k@school.edu',phone:'+91-98765-11001',status:'Active',exp:'12 yrs',classes:4,students:96,rating:4.9,joined:'2012-08-15',avatar:'AK' },
  { id:0,name:'Mr. Rajesh Gupta',subject:'English',grade:'9-12',email:'teacher1@school.edu',phone:'+91-98765-11000',status:'Active',exp:'10 yrs',classes:4,students:92,rating:4.8,joined:'2014-08-10',avatar:'RG' },
  { id:2,name:'Ms. Rohini Menon',subject:'Science',grade:'9-11',email:'rohini.m@school.edu',phone:'+91-98765-11002',status:'Active',exp:'8 yrs',classes:3,students:72,rating:4.7,joined:'2016-08-20',avatar:'RM' },
  { id:3,name:'Mr. Devendra Saha',subject:'Literature',grade:'9-12',email:'devendra.s@school.edu',phone:'+91-98765-11003',status:'Active',exp:'15 yrs',classes:5,students:120,rating:4.8,joined:'2009-08-10',avatar:'DS' },
  { id:4,name:'Mrs. Jyoti Iyer',subject:'History',grade:'10-12',email:'jyoti.i@school.edu',phone:'+91-98765-11004',status:'Active',exp:'10 yrs',classes:3,students:84,rating:4.6,joined:'2014-08-18',avatar:'JI' },
  { id:5,name:'Mr. Bhupesh Jain',subject:'Computer Sci',grade:'9-12',email:'bhupesh.j@school.edu',phone:'+91-98765-11005',status:'Active',exp:'6 yrs',classes:4,students:88,rating:4.9,joined:'2018-08-22',avatar:'BJ' },
  { id:6,name:'Ms. Oindrila Bhat',subject:'Arts',grade:'9-10',email:'oindrila.b@school.edu',phone:'+91-98765-11006',status:'On Leave',exp:'9 yrs',classes:2,students:48,rating:4.5,joined:'2015-08-19',avatar:'OB' },
  { id:7,name:'Mr. Sanjay Tripathi',subject:'Physics',grade:'10-12',email:'teacher2@school.edu',phone:'+91-98765-11007',status:'Active',exp:'11 yrs',classes:4,students:94,rating:4.8,joined:'2013-08-12',avatar:'ST' },
  { id:8,name:'Ms. Meera Nair',subject:'Hindi',grade:'9-12',email:'teacher3@school.edu',phone:'+91-98765-11008',status:'Active',exp:'9 yrs',classes:3,students:75,rating:4.7,joined:'2015-08-15',avatar:'MN' },
  { id:9,name:'Mr. Vikram Reddy',subject:'Commerce',grade:'11-12',email:'teacher4@school.edu',phone:'+91-98765-11009',status:'Active',exp:'13 yrs',classes:3,students:80,rating:4.9,joined:'2011-08-20',avatar:'VR' },
];

// ── Demo Admin Accounts ──────────────────────────────────────────────────────
const DEMO_ADMINS = [
  { email:'admin@educore.com', password:'admin123', name:'Dr. Vikram Patel' },
  { email:'admin1@educore.com', password:'admin123', name:'Mrs. Sunita Sharma' },
  { email:'admin2@educore.com', password:'admin123', name:'Mr. Arjun Verma' },
  { email:'admin3@educore.com', password:'admin123', name:'Dr. Nisha Kumar' },
  { email:'admin4@educore.com', password:'admin123', name:'Mr. Ramesh Singh' },
  { email:'admin5@educore.com', password:'admin123', name:'Ms. Priya Menon' },
  { email:'admin6@educore.com', password:'admin123', name:'Dr. Suresh Gupta' },
  { email:'admin7@educore.com', password:'admin123', name:'Mrs. Anjali Desai' },
  { email:'admin8@educore.com', password:'admin123', name:'Mr. Sameer Khan' },
  { email:'admin9@educore.com', password:'admin123', name:'Ms. Divya Iyer' },
];

const DEFAULT_CLASSES = [
  { id:1,name:'Advanced Mathematics',code:'MATH-401',teacher:'Dr. Arun Kumar',grade:'12-A',room:'B-201',time:'Mon/Wed 8:00–9:30',students:28,capacity:30,status:'Active' },
  { id:2,name:'Physics Fundamentals',code:'SCI-301',teacher:'Ms. Rohini Menon',grade:'10-B',room:'Lab-A',time:'Tue/Thu 9:00–10:30',students:24,capacity:28,status:'Active' },
  { id:3,name:'World Literature',code:'LIT-201',teacher:'Mr. Devendra Saha',grade:'11-A',room:'C-105',time:'Mon/Wed/Fri 10:00–11:00',students:30,capacity:32,status:'Active' },
  { id:4,name:'Modern History',code:'HIS-301',teacher:'Mrs. Jyoti Iyer',grade:'10-A',room:'D-302',time:'Tue/Thu 11:00–12:30',students:26,capacity:28,status:'Active' },
  { id:5,name:'Web Development',code:'CS-401',teacher:'Mr. Bhupesh Jain',grade:'12-B',room:'Tech-Lab',time:'Mon/Wed 13:00–14:30',students:22,capacity:25,status:'Active' },
  { id:6,name:'Studio Arts',code:'ART-201',teacher:'Ms. Oindrila Bhat',grade:'9-A',room:'Art-Studio',time:'Fri 13:00–16:00',students:18,capacity:20,status:'Paused' },
  { id:7,name:'Algebra II',code:'MATH-301',teacher:'Dr. Arun Kumar',grade:'10-C',room:'B-102',time:'Tue/Thu 8:00–9:30',students:30,capacity:30,status:'Active' },
];

const DEFAULT_ATTENDANCE = [
  { date:'2024-12-02',class:'Advanced Mathematics',present:26,absent:2,late:0,total:28 },
  { date:'2024-12-02',class:'Physics Fundamentals',present:22,absent:1,late:1,total:24 },
  { date:'2024-12-02',class:'World Literature',present:28,absent:2,late:0,total:30 },
  { date:'2024-12-03',class:'Modern History',present:25,absent:1,late:0,total:26 },
  { date:'2024-12-03',class:'Web Development',present:20,absent:1,late:1,total:22 },
  { date:'2024-12-04',class:'Advanced Mathematics',present:27,absent:1,late:0,total:28 },
  { date:'2024-12-04',class:'Physics Fundamentals',present:23,absent:0,late:1,total:24 },
];

// ── Data Store ─────────────────────────────────────────────────────────────
function getStudents() { return JSON.parse(localStorage.getItem('edu_students') || JSON.stringify(DEFAULT_STUDENTS)); }
function saveStudents(data) { localStorage.setItem('edu_students', JSON.stringify(data)); }
function getTeachers() { return JSON.parse(localStorage.getItem('edu_teachers') || JSON.stringify(DEFAULT_TEACHERS)); }
function getClasses() { return JSON.parse(localStorage.getItem('edu_classes') || JSON.stringify(DEFAULT_CLASSES)); }
function getAttendance() { return JSON.parse(localStorage.getItem('edu_attendance') || JSON.stringify(DEFAULT_ATTENDANCE)); }

// ── Load data from accounts.json ────────────────────────────────────────────
async function loadAccountsData() {
  try {
    const response = await fetch('accounts.json?t=' + Date.now());
    const data = await response.json();
    if (data.students && data.students.length > 0) {
      // Ensure all students have IDs
      data.students.forEach((s, idx) => {
        if (!s.id) s.id = idx + 1;
      });
      localStorage.setItem('edu_students', JSON.stringify(data.students));
      localStorage.setItem('edu_teachers', JSON.stringify(data.teachers || DEFAULT_TEACHERS));
      localStorage.setItem('edu_admins', JSON.stringify(data.admins || DEMO_ADMINS));
    }
  } catch (e) {
    console.warn('Could not load accounts.json, using defaults:', e);
  }
}

loadAccountsData();
function getNotifications() {
  return [
    { id:1, text:'New student enrollment: Mohit Verma', time:'2 min ago', type:'info', read:false },
    { id:2, text:'Attendance below 75%: Nikhil Singh', time:'1 hr ago', type:'warning', read:false },
    { id:3, text:'Parent meeting scheduled: Sharma family', time:'3 hrs ago', type:'info', read:true },
    { id:4, text:'Grade reports due this Friday', time:'1 day ago', type:'alert', read:true },
  ];
}

// ── Global Toggle Function ───────────────────────────────────────────────────
function toggleSidebar(){
  const s=document.getElementById('sidebar');
  const o=document.getElementById('sidebarOverlay');
  if(s && o){
    s.classList.toggle('-translate-x-full');
    o.classList.toggle('hidden');
  }
}

// ── Sidebar HTML ────────────────────────────────────────────────────────────
function renderSidebar(activePage) {
  const user = authGuard();
  const nav = [
    { href:'dashboard.html', icon:'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6', label:'Dashboard', id:'dashboard' },
    { href:'students.html', icon:'M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z', label:'Students', id:'students' },
    { href:'teachers.html', icon:'M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z', label:'Teachers', id:'teachers' },
    { href:'classes.html', icon:'M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10', label:'Classes', id:'classes' },
    { href:'attendance.html', icon:'M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4', label:'Attendance', id:'attendance' },
    { href:'settings.html', icon:'M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z M15 12a3 3 0 11-6 0 3 3 0 016 0z', label:'Settings', id:'settings' },
  ];

  const students = getStudents();
  const notifs = getNotifications().filter(n=>!n.read).length;

  return `
  <!-- Mobile overlay -->
  <div id="sidebarOverlay" class="fixed inset-0 bg-black/60 z-30 hidden lg:hidden pointer-events-auto" onclick="toggleSidebar()"></div>

  <!-- Sidebar -->
  <aside id="sidebar" class="fixed left-0 top-0 h-full w-64 bg-navy-900 border-r border-white/5 z-40 transform -translate-x-full lg:translate-x-0 transition-transform duration-300 flex flex-col">
    <!-- Logo -->
    <div class="p-6 border-b border-white/5">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-teal-400 to-teal-600 flex items-center justify-center shadow-lg shadow-teal-500/30">
          <svg class="w-5 h-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
        </div>
        <div>
          <div class="display text-white font-bold text-lg leading-tight">Parvati High School</div>
          <div class="text-teal-400 text-xs font-semibold">Bikram</div>
        </div>
      </div>
    </div>

    <!-- User -->
    <div class="px-4 py-4 border-b border-white/5">
      <div class="flex items-center gap-3 px-3 py-2.5 rounded-xl bg-white/5">
        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-teal-400 to-teal-600 flex items-center justify-center text-white text-xs font-bold flex-shrink-0">${user.avatar||'SA'}</div>
        <div class="overflow-hidden">
          <div class="text-white text-sm font-medium truncate">${user.name}</div>
          <div class="text-slate-500 text-xs">${user.role}</div>
        </div>
      </div>
    </div>

    <!-- Nav -->
    <nav class="flex-1 px-4 py-4 space-y-1 overflow-y-auto">
      <p class="text-slate-600 text-xs uppercase tracking-wider px-3 mb-2 font-semibold">Main Menu</p>
      ${nav.map(item => {
        const active = item.id === activePage;
        return `<a href="${item.href}" class="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all duration-200 ${active ? 'bg-teal-500/15 text-teal-400 border border-teal-500/20' : 'text-slate-400 hover:text-white hover:bg-white/5'}">
          <svg class="w-4 h-4 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.75" d="${item.icon}"/></svg>
          <span>${item.label}</span>
          ${item.id==='students'?`<span class="ml-auto text-xs bg-teal-500/20 text-teal-400 px-1.5 py-0.5 rounded-md">${students.length}</span>`:''}
        </a>`;
      }).join('')}
    </nav>

    <!-- Bottom -->
    <div class="p-4 border-t border-white/5">
      <button onclick="logout()" class="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-slate-400 hover:text-coral-400 hover:bg-coral-500/10 transition-all text-sm font-medium">
        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
        Logout
      </button>
    </div>
  </aside>
  `;
}

// ── Topbar HTML ─────────────────────────────────────────────────────────────
function renderTopbar(title, subtitle) {
  const notifs = getNotifications();
  const unread = notifs.filter(n=>!n.read).length;
  return `
  <header class="h-16 bg-navy-900/80 backdrop-blur-xl border-b border-white/5 flex items-center px-4 sm:px-6 gap-4 sticky top-0 z-20">
    <button type="button" onclick="toggleSidebar()" class="lg:hidden text-slate-400 hover:text-white transition-colors p-2 -m-2 pointer-events-auto">
      <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
    </button>
    <div class="flex-1">
      <h1 class="display text-white font-bold text-lg leading-tight">${title}</h1>
      <p class="text-slate-500 text-xs">${subtitle}</p>
    </div>
    <div class="flex items-center gap-3">
      <!-- Search -->
      <div class="hidden md:flex items-center gap-2 bg-white/5 border border-white/10 rounded-xl px-3 py-1.5 w-48">
        <svg class="w-4 h-4 text-slate-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
        <input type="text" placeholder="Search..." class="bg-transparent text-slate-300 text-xs outline-none w-full placeholder-slate-600"/>
      </div>
      <!-- Notifs -->
      <div class="relative">
        <button class="w-9 h-9 rounded-xl bg-white/5 border border-white/10 flex items-center justify-center text-slate-400 hover:text-teal-400 transition-colors" onclick="document.getElementById('notifPanel').classList.toggle('hidden')">
          <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
          ${unread>0?`<span class="absolute -top-1 -right-1 w-4 h-4 bg-coral-500 rounded-full text-white text-xs flex items-center justify-center leading-none">${unread}</span>`:''}
        </button>
        <div id="notifPanel" class="hidden absolute right-0 top-12 w-80 bg-navy-800 border border-white/10 rounded-2xl shadow-2xl z-50 overflow-hidden">
          <div class="p-4 border-b border-white/5"><p class="text-white text-sm font-semibold">Notifications</p></div>
          ${notifs.map(n=>`
          <div class="px-4 py-3 border-b border-white/5 hover:bg-white/5 transition-colors flex gap-3 ${n.read?'opacity-50':''}">
            <div class="w-2 h-2 rounded-full mt-1.5 flex-shrink-0 ${n.type==='warning'?'bg-amber-400':n.type==='alert'?'bg-coral-400':'bg-teal-400'}"></div>
            <div><p class="text-slate-300 text-xs">${n.text}</p><p class="text-slate-600 text-xs mt-0.5">${n.time}</p></div>
          </div>`).join('')}
        </div>
      </div>
    </div>
  </header>`;
}
