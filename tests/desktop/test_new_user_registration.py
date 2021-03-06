#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from unittestzero import Assert
from pages.desktop.register_page import RegisterPage
import pytest


class TestNewUserRegistration:

    @pytest.mark.fft
    def test_that_thank_you_page_is_displayed_after_successful_registration(self, mozwebqa):
        """
           Register a new user using random username.
           Verify registration by checking the page title
        """
        register_pg = RegisterPage(mozwebqa)
        register_pg.go_to_registration_page()
        register_pg.register_new_user()
        actual_page_title = register_pg.page_title
        expected_page_title = register_pg._page_title_after_registration
        Assert.contains(expected_page_title, actual_page_title)
