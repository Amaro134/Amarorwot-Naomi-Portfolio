from django.shortcuts import render


def index(request):

    projects = [
        {
            "title": "Beyond Sports",
            "description": "Corporate Wellness Platform featuring scalable backend services, JWT authentication, and secure API endpoints. Integrated Claude Vision OCR for AI-powered workout data extraction with SHA-256 deduplication.",
            "tags": ["NestJS", "React", "PostgreSQL", "Prisma", "TypeScript"],
            "color": "beyond",
            "live_url": "https://beyondsports.fitness/",
            "github_url": "https://github.com/Amaro134",
        },
        {
            "title": "My Grocery Buddy",
            "description": "Production-ready full-stack grocery management app with authentication, CRUD, search, PDF/CSV export, and a statistics dashboard. Validated across 3 device breakpoints.",
            "tags": ["Python", "Django", "PostgreSQL", "REST API"],
            "color": "grocery",
            "live_url": "#",
            "github_url": "https://github.com/Amaro134",
        },
        {
            "title": "MindEase",
            "description": "Mental wellness platform for the East African market. Built after user interviews with 15+ Kampala users uncovering stigma as the key barrier. Features anonymous mood logging, analytics dashboard, and self-paced wellness content.",
            "tags": ["Python", "Django", "PostgreSQL", "Render", "CI/CD"],
            "color": "mindease",
            "live_url": "https://mindease-xwgc.onrender.com",
            "github_url": "https://github.com/Amaro134",
        },
        {
            "title": "Mayondo Wood & Furniture Management System",
            "description": "A full-featured web application built with a focus on clean architecture and user-centric design. Scalable backend with RESTful APIs and a responsive, intuitive frontend.",
            "tags": ["React", "Node.js", "PostgreSQL", "TypeScript"],
            "color": "mayondo",
            "live_url": "#",
            "github_url": "https://github.com/Amaro134",
        },
        {
            "title": "Kampala EEG Lab & Sleep Center",
            "description": "Full production web application for a medical diagnostic clinic, including a multi-step patient booking system, JWT-authenticated admin dashboard with role-based access control, OTP password reset, and automated email notifications. Deployed on a live custom domain with CI/CD auto-deployment.",
            "tags": ["React", "NestJS", "Prisma", "PostgreSQL", "TypeScript", "DigitalOcean"],
            "color": "kampala",
            "live_url": "https://kampalaeeglabandsleepcenter.ug",
            "github_url": "https://github.com/Amaro134",
        },
    ]

    designs = [
        {
            "title": "Grocery Buddy",
            "description": "Full UX/UI design for a grocery management app with intuitive CRUD flows, search, and a statistics dashboard. Designed for clarity across mobile and desktop breakpoints.",
            "tags": ["Figma", "UX Design", "Mobile", "Dashboard"],
            "image_url": "https://drive.google.com/file/d/1Bgt5IfejGX-2aJNGnM1lbOkGMtVL4JtL/view?usp=sharing",
            "figma_url": "https://www.figma.com/design/khc9MZCcBoxiQMqG0lzByQ/Grocery-buddy?node-id=0-1&m=dev&t=0XSUXzY3uunRC4I6-1",
        },
        {
            "title": "MindEase App Design",
            "description": "End-to-end UX/UI design for a mental wellness platform targeting East African users. Focused on reducing stigma through calm, approachable visuals and simple onboarding flows.",
            "tags": ["Figma", "UX Research", "Mobile Design"],
            "image_url": "",
            "figma_url": "https://www.figma.com/design/uMa7xshPu0F87dU3tF811v/MindEase?node-id=0-1&m=dev&t=cKqfMxOPEwNGksAp-1",
        },
        {
            "title": "Kampala EEG Lab Patient Portal",
            "description": "Designed the patient-facing booking interface and admin dashboard for a medical diagnostic center. Prioritised clarity and trust through clean layouts and accessible colour choices.",
            "tags": ["Figma", "Healthcare UX", "Dashboard Design"],
            "image_url": "",
            "figma_url": "https://www.figma.com/design/2nLJ02qChlztxmXAfFu0uj/Kampala-EEG-Labs?node-id=0-1&m=dev&t=RTw89YOcatiyFBQ0-1",
        },
    ]
    skills = {
        "frontend": [
            {"name": "React.js"}, {"name": "React Native"},
            {"name": "TypeScript"}, {"name": "HTML/CSS3"},
        ],
        "backend": [
            {"name": "Node.js"}, {"name": "NestJS"},
            {"name": "Python"}, {"name": "Django"},
        ],
        "data": [
            {"name": "PostgreSQL"}, {"name": "Prisma ORM"},
            {"name": "Supabase"}, {"name": "SQL"}, {"name": "Neon"},
        ],
        "tools": [
            {"name": "Docker"}, {"name": "Azure"}, {"name": "Digital Ocean"},
            {"name": "Render"}, {"name": "Vercel"}, {"name": "CI/CD"},
            {"name": "Git"}, {"name": "Firebase"}, {"name": "Google Cloud Console"},
            {"name": "Figma"}, {"name": "Lean and Agile"},
        ],
    }

    stats = [
        {"value": "6+",  "label": "Production APIs Delivered"},
        {"value": "3+",  "label": "Frameworks Mastered"},
        {"value": "4",   "label": "Shipped Projects"},
        {"value": "15+", "label": "User Interviews Conducted"},
    ]

    experiences = [
        {
            "title": "Full Stack Developer Apprentice",
            "company": "Refactory Academy — Beyond Sports",
            "location": "Kampala, Uganda",
            "start_date": "Oct 2025",
            "end_date": "Present",
            "is_current": True,
            "bullets": [
                "Delivered 6+ production-ready RESTful APIs for the Beyond Sports platform using NestJS.",
                "Built and shipped multiple React.js dashboard pages and components.",
                "Integrated Claude Vision OCR and migrated to expo-notifications in React Native app.",
                "Tracked post-release performance across 15+ screens, reducing visible defects by ~60%.",
                "Participated in code reviews, sprint planning, and agile development processes.",
            ],
        },
        {
            "title": "Freelance Full Stack Developer",
            "company": "Kampala EEG Lab & Sleep Center",
            "location": "Kampala, Uganda",
            "start_date": "2026",
            "end_date": "2026",
            "is_current": False,
            "bullets": [
                "Designed and built a full production web application from scratch for a medical diagnostic clinic.",
                "Implemented a multi-step patient booking flow with JWT authentication and OTP password reset.",
                "Built an admin dashboard with role-based access control for managing appointments and staff accounts.",
                "Integrated transactional emails via Brevo for booking confirmations, OTP delivery, and admin onboarding.",
                "Deployed the full stack on a DigitalOcean droplet with a custom domain, SSL, and CI/CD via GitHub Actions.",
            ],
        },
    ]

    context = {
        "projects": projects,
        "designs": designs,
        "skills": skills,
        "stats": stats,
        "experiences": experiences,
    }
    return render(request, "name/index.html", context)