from hamcrest import assert_that


def test_home_page_is_displayed(once_user_is_logged_in):
    assert_that(once_user_is_logged_in.is_welcome_message_present() is True)
