#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.community import CommunityPage
from pages.home import HomePage


class TestCommunityPage:

    @pytest.mark.nondestructive
    def test_community_title(self, mozwebqa):
        home_page = HomePage(mozwebqa)
        home_page.go_to_home_page()
        community_page = home_page.header_region.click_community_link()
        Assert.true(community_page.is_the_current_page)
