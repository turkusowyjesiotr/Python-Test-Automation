import pytest
from pages.iframe_page import IframePage


@pytest.mark.usefixtures('setup')
class TestIframe:
    def test_iframe(self):
        page = IframePage()
        assert page.is_main_page_open(), 'Main page is not open'
        page.click_alerts_card()
        page.click_nested_frames_button()
        assert page.is_page_with_nested_frames_open(), 'Nested Frames form not open'
        assert page.get_parent_frame_text(self.driver) == 'Parent frame', 'Parent frame message not present'
        assert page.get_child_frame_text(self.driver) == 'Child Iframe', 'Child Iframe message not present'
        page.click_frames_button(self.driver)
        assert page.is_page_with_frames_open(), 'Frames page is not open'
        upper_frame_text = page.get_upper_frame_text(self.driver)
        lower_frame_text = page.get_lower_frame_text(self.driver)
        assert upper_frame_text == lower_frame_text, 'Strings in upper and lower frame do not match'
