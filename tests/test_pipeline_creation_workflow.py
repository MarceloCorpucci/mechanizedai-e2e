from hamcrest import assert_that


def test_home_page_is_displayed(once_user_is_logged_in):
    assert_that(once_user_is_logged_in.is_welcome_message_present() is True)


def test_pipeline_page_is_displayed(once_user_is_logged_in):
    pipeline_page_displayed = once_user_is_logged_in \
        .go_to_mechanized_insights() \
        .go_to_pipelines() \
        .is_pipeline_page_displayed()

    assert_that(pipeline_page_displayed is True)


def test_user_creates_a_new_pipeline(once_user_is_logged_in):
    # TODO: Another pre condition is needed to create an Application,
    #  which is required for this scenario to be executed properly.
    once_user_is_logged_in \
        .go_to_mechanized_insights() \
        .go_to_pipelines() \
        .select_application() \
        .go_to_create_pipeline_page() \
        .create('test1')
