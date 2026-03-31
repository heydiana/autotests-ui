import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(chromium_page_with_state):
    page = chromium_page_with_state

    courses_list_page = CoursesListPage(page)
    create_course_page = CreateCoursePage(page)

    # открыть создание курсов
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # проверки до заполнения
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)

    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # загрузка изображения
    image_path = "./testdata/files/image.jpeg"
    create_course_page.upload_preview_image(image_path)

    # проверка после загрузки
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # заполнение формы
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )

    # создание курса
    create_course_page.click_create_course_button()

    # проверки на странице списка
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    courses_list_page.check_visible_course_card(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )