import pytest
from playwright.sync_api import expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    expect(page.get_by_test_id("courses-list-toolbar-title-text")).to_have_text("Courses")

    expect(page.get_by_test_id("courses-list-empty-view-title-text")).to_have_text("There is no results")

    expect(page.get_by_test_id("courses-list-empty-view-icon")).to_be_visible()

    expect(
        page.get_by_test_id("courses-list-empty-view-description-text")
    ).to_have_text("Results from the load test pipeline will be displayed here")