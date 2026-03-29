from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.courses_title = page.get_by_test_id('courses-widget-title-text')
        self.courses_image = page.get_by_test_id('courses-preview-image')
        self.courses_max_text = page.get_by_test_id('courses-max-score-info-row-view-text')
        self.courses_min_text = page.get_by_test_id('courses-min-score-info-row-view-text')
        self.courses_estimated_time_text = page.get_by_test_id('courses-estimated-time-info-row-view-text')

        self.courses_menu_button = page.get_by_test_id('courses-view-menu-button')
        self.courses_edit_menu_button = page.get_by_test_id('courses-view-edit-menu-item')
        self.courses_delete_button = page.get_by_test_id('courses-view-delete-menu-item')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-title-text')




    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text("There is no results")

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_create_course_button(self):
        expect(self.create_course_button).to_be_visible()


    def check_visible_course_card(
            self,
            index: int,  # Индекс карточки в списке курсов
            title: str,  # Ожидаемый заголовок курса
            max_score: str,  # Ожидаемый максимальный балл
            min_score: str,  # Ожидаемый минимальный балл
            estimated_time: str  # Ожидаемое время прохождения
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_max_score_text.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.course_min_score_text.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(
            f"Estimated time: {estimated_time}"
        )

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_button_menu_item.nth(index)).to_be_visible()
        self.course_edit_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_button.nth(index)).to_be_visible()
        self.course_delete_menu_button.nth(index).click()


