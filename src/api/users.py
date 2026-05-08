
from fastapi import APIRouter, Request,Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from src.bitrix_service import create_bitrix_lead
from src.database import engine,Base
from src.api.dependenceis import SessionDep
from datetime import datetime
from src.models.users import UserModel
from src.schemas.users import UserAddSchema
router =APIRouter()
from src.models.users import UserModel
from src.models.resume import Resume
from src.models.vacancy import Vacancy
from src.models.interview import Interview
from src.models.skills import SkillModel
from src.models.Answers import AnswerModel
from src.models.preparation_plans import PreparationPlanModel
templates = Jinja2Templates(directory="src/templates")


@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@router.post("/register")
async def add_user(
    full_name: str = Form(...),
    email: str = Form(...),
    password_hash: str = Form(...),
    target_position: str = Form(""),
    session: SessionDep = None
):
    new_user = UserModel(
        full_name=full_name,
        email=email,
        password_hash=password_hash,
        target_position=target_position,
        account_status="active"
    )
    session.add(new_user)
    await session.commit()
    create_bitrix_lead(new_user)
    print("BITRIX FUNCTION CALLED")

    return RedirectResponse(url="/dashboard", status_code=303)




@router.get("/auth", response_class=HTMLResponse)
async def get_auth_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="auth.html",
        context={"request": request}
    )


@router.post("/seed_database")
async def seed_database(session: SessionDep):
    # USERS
    user1 = UserModel(
        full_name="Иван Иванов",
        email="ivan11111@mail.ru",
        password_hash="123",
        role="candidate",
        target_position="Python Developer",
        account_status="active"
    )
    user2 = UserModel(
        full_name="Анна Смирнова",
        email="anna2@mail.ru",
        password_hash="123",
        role="candidate",
        target_position="Backend Developer",
        account_status="active"
    )
    user3 = UserModel(
        full_name="Дмитрий Петров",
        email="dmitry3@mail.ru",
        password_hash="123",
        role="candidate",
        target_position="Data Analyst",
        account_status="active"
    )

    session.add_all([user1, user2, user3])
    await session.commit()
    await session.refresh(user1)
    await session.refresh(user2)
    await session.refresh(user3)

    # RESUMES
    resume1 = Resume(
        user_id=user1.user_id,
        file_name="ivan_resume.pdf",
        resume_text="Python, FastAPI, SQLAlchemy, PostgreSQL",
        education="РЭУ им. Плеханова",
        experience="1 год стажировки в IT-компании",
        resume_status="uploaded"
    )
    resume2 = Resume(
        user_id=user2.user_id,
        file_name="anna_resume.pdf",
        resume_text="Java, Spring, SQL, Docker",
        education="МГУ",
        experience="2 года backend-разработки",
        resume_status="uploaded"
    )
    resume3 = Resume(
        user_id=user3.user_id,
        file_name="dmitry_resume.pdf",
        resume_text="Python, Pandas, Power BI, Excel",
        education="НГУ",
        experience="1.5 года аналитики данных",
        resume_status="uploaded"
    )

    session.add_all([resume1, resume2, resume3])
    await session.commit()
    await session.refresh(resume1)
    await session.refresh(resume2)
    await session.refresh(resume3)

    # VACANCIES
    vacancy1 = Vacancy(
        user_id=user1.user_id,
        job_title="Junior Python Developer",
        company_name="TechSoft",
        vacancy_text="Требуется знание Python, FastAPI, SQL",
        level="junior",
        source_link="https://example.com/vacancy1"
    )
    vacancy2 = Vacancy(
        user_id=user2.user_id,
        job_title="Backend Developer",
        company_name="CloudSystems",
        vacancy_text="Нужны Java, Spring, Docker, REST API",
        level="middle",
        source_link="https://example.com/vacancy2"
    )
    vacancy3 = Vacancy(
        user_id=user3.user_id,
        job_title="Data Analyst",
        company_name="DataVision",
        vacancy_text="Требуются Python, SQL, аналитика данных",
        level="junior",
        source_link="https://example.com/vacancy3"
    )

    session.add_all([vacancy1, vacancy2, vacancy3])
    await session.commit()
    await session.refresh(vacancy1)
    await session.refresh(vacancy2)
    await session.refresh(vacancy3)

    # SKILLS
    skill1 = SkillModel(
        skill_name="Python",
        skill_category="Programming Language",
        skill_level="Intermediate",
        source_type="resume",
        description="Язык программирования для backend и аналитики"
    )
    skill2 = SkillModel(
        skill_name="FastAPI",
        skill_category="Framework",
        skill_level="Beginner",
        source_type="vacancy",
        description="Фреймворк для разработки API на Python"
    )
    skill3 = SkillModel(
        skill_name="SQL",
        skill_category="Database",
        skill_level="Intermediate",
        source_type="resume",
        description="Язык запросов к реляционным базам данных"
    )

    session.add_all([skill1, skill2, skill3])
    await session.commit()
    await session.refresh(skill1)
    await session.refresh(skill2)
    await session.refresh(skill3)

    # INTERVIEWS
    interview1 = Interview(
        user_id=user1.user_id,
        vacancy_id=vacancy1.vacancy_id,
        interview_type="Technical Interview",
        difficulty_level="medium",
        started_at=datetime.utcnow(),
        finished_at=datetime.utcnow(),
        score=7,
        interview_status="completed"
    )
    interview2 = Interview(
        user_id=user2.user_id,
        vacancy_id=vacancy2.vacancy_id,
        interview_type="HR Interview",
        difficulty_level="easy",
        started_at=datetime.utcnow(),
        finished_at=datetime.utcnow(),
        score=8,
        interview_status="completed"
    )
    interview3 = Interview(
        user_id=user3.user_id,
        vacancy_id=vacancy3.vacancy_id,
        interview_type="AI Interview",
        difficulty_level="hard",
        started_at=datetime.utcnow(),
        finished_at=datetime.utcnow(),
        score=6,
        interview_status="completed"
    )

    session.add_all([interview1, interview2, interview3])
    await session.commit()
    await session.refresh(interview1)
    await session.refresh(interview2)
    await session.refresh(interview3)

    # ANSWERS
    answer1 = AnswerModel(
        interview_id=interview1.interview_id,
        question_text="Что такое FastAPI?",
        answer_text="Это современный Python-фреймворк для создания API.",
        answer_score=8,
        feedback_text="Ответ корректный, но можно было привести примеры использования."
    )
    answer2 = AnswerModel(
        interview_id=interview2.interview_id,
        question_text="Почему вы хотите работать в нашей компании?",
        answer_text="Мне интересны ваши проекты и возможность профессионального роста.",
        answer_score=7,
        feedback_text="Ответ хороший, но немного общий."
    )
    answer3 = AnswerModel(
        interview_id=interview3.interview_id,
        question_text="Чем отличается LEFT JOIN от INNER JOIN?",
        answer_text="INNER JOIN возвращает общие строки, LEFT JOIN — все строки из левой таблицы.",
        answer_score=9,
        feedback_text="Ответ точный и содержательный."
    )

    session.add_all([answer1, answer2, answer3])
    await session.commit()
    await session.refresh(answer1)
    await session.refresh(answer2)
    await session.refresh(answer3)

    # PREPARATION PLANS
    plan1 = PreparationPlanModel(
        user_id=user1.user_id,
        vacancy_id=vacancy1.vacancy_id,
        weak_topics="Асинхронность, ORM",
        recommended_topics="async/await, SQLAlchemy relationships",
        priority_level="high",
        plan_status="generated"
    )
    plan2 = PreparationPlanModel(
        user_id=user2.user_id,
        vacancy_id=vacancy2.vacancy_id,
        weak_topics="Docker, микросервисы",
        recommended_topics="Docker Compose, REST architecture",
        priority_level="medium",
        plan_status="generated"
    )
    plan3 = PreparationPlanModel(
        user_id=user3.user_id,
        vacancy_id=vacancy3.vacancy_id,
        weak_topics="SQL joins, визуализация",
        recommended_topics="JOIN, Power BI dashboards",
        priority_level="high",
        plan_status="generated"
    )

    session.add_all([plan1, plan2, plan3])
    await session.commit()

    return {"ok": True, "message": "Тестовые данные успешно добавлены"}