<div class="iframe">

</div>

<div style="background-color: #ffced4; padding: 2em; text-align: center; font-size: 18px;">

For full functionality, please enable Javascript.

</div>

<div style="position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0;">

Suunto is committed to achieving Level AA conformance for this website
in conformance with the Web Content Accessibility Guidelines (WCAG) 2.0
and achieving compliance with other accessibility standards. Please
contact Customer Service at USA +1 855 258 0900 (toll free), if you have
any issues accessing information on this website.

</div>

<div id="app" v-cloak="">

<div class="notification-container">

</div>

<div class="header u-width-100" role="banner"
:class="['', { 'mobile' : !$mq.laptop }]">

<div class="notification-bar" v-if="$mq.laptop &amp;&amp; !false">

<div class="notification-bar__wrapper f-center">

</div>

</div>

<div class="container-fluid wrapper" v-show="$mq.laptop">

<div class="navigation__logo-container">

</div>

<div class="u-flex u-flex-1 u-flex-valign-baseline">

- <div v-if="!loginScope.isLoading">

  <div v-if="loginScope.isVipLoginVisible"
  @click.prevent.stop="slotScope.toggleSubMenu('Profile')">

  </div>

  <div v-else="">

  </div>

  </div>

  <div class="u-flex m-md" v-if="!loginScope.isVipLoginVisible">

  <a href="#login-modal"
  class="header__signin u-flex u-flex-valign-center u-flex-center"
  data-header-mobile-signin=""
  data-@click.prevent.stop="loginScope.openLoginModal()"><span
  class="f-13 f-black f-uppercase f-bold">Sign in</span></a>

  </div>

</div>

</div>

<div class="navigation-mobile__wrapper u-flex">

<div class="navigation-mobile__header u-flex u-flex-valign-center"
:class="{ 'is-active': slotScope.isMenuOrSearchOpen }">

<div class="hamburger-box">

<div class="hamburger-inner">

</div>

</div>

<div class="u-flex u-width-100 u-flex-center">

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpenSearch">

<div class="navigation-mobile__menu"
:class="{ 'is-open': slotScope.isOpenSearch }">

Search

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpenProfile">

<div class="navigation-mobile__menu"
:class="{ 'is-open': slotScope.isOpenProfile }">

<div class="u-flex u-flex-dir-column"
v-if="!loginScope.isVipLoginVisible">

<div class="m-md">

<a href="#login-modal"
class="header__signin u-flex u-flex-valign-center u-flex-center"
data-header-mobile-signin=""
data-@click.prevent.stop="loginScope.openLoginModal(slotScope.toggleProfile)"><span
class="f-13 f-black f-uppercase f-bold">Sign in</span></a>

</div>

</div>

</div>

</div>

<div class="sidebar-panel" v-if="slotScope.isOpen">

<div class="navigation-mobile__menu">

</div>

</div>

</div>

</div>

<div class="manual-page u-bg-light-gray">

<div class="container-fluid wrapper">

<div class="row u-bg-white">

<div class="col-xs-12 breadcrumb breadcrumb--top">

- [Home](/)
- [Support](/Support/)
- [Suunto 7](/Support/sports-watches-support/suunto-7/)
- [User Guide](/Support/Product-support/suunto_7/suunto_7/)

</div>

</div>

<div class="row u-bg-light-gray">

<div class="col-xs-12 manual-page__page-title">

# Suunto 7 User Guide

</div>

</div>

<div class="row u-bg-white u-relative">

<div class="col-xs-12 manual-page__content-wrapper u-relative p-0 u-flex">

<div class="manual-page__sidebar-wrapper">

<div role="button" tabindex="0" @click.prevent.stop="slotScope.toggle"
:class="['canvas', {'active' : slotScope.isOpen}]">

</div>

<div class="sidebar__wrapper u-bg-white">

<div class="sidebar__heading f-16 u-width-100 visible-from-md">

Table of Content

</div>

<div class="sidebar__heading f-16 u-width-100 u-flex-valign-center u-flex-justify-space-between"
role="button" tabindex="0" @click.prevent.stop="slotScope.toggle"
@keydown.enter.prevent.stop="slotScope.toggle"
@keydown.space.prevent.stop="slotScope.toggle">

Table of Content
<span :class="['f-26 suunto-icon suunto-icon-list-view', { 'f-brand' : slotScope.isOpen }]"></span>

</div>

<div class="menu sidebar-menu">

<div class="menu__item">

[Start](https://www.suunto.com/Support/Product-support/suunto_7/suunto_7/)

</div>

<div class="menu__item">

[Welcome](/Support/Product-support/suunto_7/suunto_7/welcome/)

</div>

<div class="menu">

<div class="menu__item">

[Your Suunto
7](/Support/Product-support/suunto_7/suunto_7/get-started/your-suunto-7/)

</div>

<div class="menu__item">

[Set up and pair your Suunto
7](/Support/Product-support/suunto_7/suunto_7/get-started/set-up-and-pair-your-suunto-7/)

</div>

<div class="menu__item">

[Change
language](/Support/Product-support/suunto_7/suunto_7/get-started/change-language/)

</div>

<div class="menu__item">

[Charge your
watch](/Support/Product-support/suunto_7/suunto_7/get-started/charge-your-watch/)

</div>

<div class="menu__item">

[Learn to navigate your Suunto
7](/Support/Product-support/suunto_7/suunto_7/get-started/learn-to-navigate-your-suunto-7/)

</div>

<div class="menu__item">

[Wake up your
display](/Support/Product-support/suunto_7/suunto_7/get-started/wake-up-your-display/)

</div>

<div class="menu__item">

[Connect to the
Internet](/Support/Product-support/suunto_7/suunto_7/get-started/connect-to-the-internet/)

</div>

<div class="menu__item">

[Keep your Suunto 7 up to
date](/Support/Product-support/suunto_7/suunto_7/get-started/keep-your-suunto-7-up-to-date/)

</div>

<div class="menu__item">

[Set an
alarm](/Support/Product-support/suunto_7/suunto_7/get-started/set-an-alarm/)

</div>

<div class="menu__item">

[Turn your watch on and
off](/Support/Product-support/suunto_7/suunto_7/get-started/turn-your-watch-on-and-off/)

</div>

<div class="menu__item">

[Restart your
watch](/Support/Product-support/suunto_7/suunto_7/get-started/restart-your-watch/)

</div>

<div class="menu__item">

[Reset your watch to factory
settings](/Support/Product-support/suunto_7/suunto_7/get-started/reset-your-watch-to-factory-settings/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Google
Pay](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/google-pay/)

</div>

<div class="menu__item">

[Google
Fit](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/google-fit/)

</div>

<div class="menu__item">

[Google Play
Store](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/google-play-store/)

</div>

<div class="menu__item">

[Use and manage
apps](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/use-and-manage-apps/)

</div>

<div class="menu__item">

[Get notifications on your
watch](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/get-notifications-on-your-watch/)

</div>

<div class="menu__item">

[View and manage your
Tiles](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/view-and-manage-your-tiles/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Customize watch
faces](/Support/Product-support/suunto_7/suunto_7/customize-your-watch/customize-watch-faces/)

</div>

<div class="menu__item">

[Customize button
shortcuts](/Support/Product-support/suunto_7/suunto_7/customize-your-watch/customize-button-shortcuts/)

</div>

<div class="menu__item">

[Change watch
straps](/Support/Product-support/suunto_7/suunto_7/customize-your-watch/change-watch-straps/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Suunto Wear app on your
watch](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/suunto-wear-app-on-your-watch/)

</div>

<div class="menu__item">

[Suunto mobile app on your
phone](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/suunto-mobile-app-on-your-phone/)

</div>

<div class="menu__item">

[Suunto
maps](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/suunto-maps/)

</div>

<div class="menu__item">

[Different sports and
measurements](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/different-sports-and-measurements/)

</div>

<div class="menu__item">

[Start an
exercise](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/start-an-exercise/)

</div>

<div class="menu__item">

[Control watch during
exercise](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/control-watch-during-exercise/)

</div>

<div class="menu__item">

[Pause and resume
exercise](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/pause-and-resume-exercise/)

</div>

<div class="menu__item">

[End and review
exercise](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/end-and-review-exercise/)

</div>

<div class="menu__item">

[Swimming with Suunto
7](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/swimming-with-suunto-7/)

</div>

<div class="menu__item">

[Exercise with
maps](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/exercise-with-maps/)

</div>

<div class="menu__item">

[Route
navigation](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/route-navigation/)

</div>

<div class="menu__item">

[Exercise with
music](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/exercise-with-music/)

</div>

<div class="menu__item">

[Exercise
options](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/exercise-options/)

</div>

<div class="menu__item">

[Map
options](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/map-options/)

</div>

<div class="menu__item">

[General
options](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/general-options/)

</div>

<div class="menu__item">

[Diary](/Support/Product-support/suunto_7/suunto_7/sports-by-suunto/diary/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Follow your heart rate with Suunto
7](/Support/Product-support/suunto_7/suunto_7/heart-rate/follow-your-heart-rate-with-suunto-7/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Daily heart
rate](/Support/Product-support/suunto_7/suunto_7/activity-tracking/daily-heart-rate/)

</div>

<div class="menu__item">

[Body
resources](/Support/Product-support/suunto_7/suunto_7/activity-tracking/body-resources/)

</div>

<div class="menu__item">

[Turn on Daily heart rate &
resources](/Support/Product-support/suunto_7/suunto_7/activity-tracking/turn-on-daily-heart-rate--resources-/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Turn sleep tracking
on](/Support/Product-support/suunto_7/suunto_7/sleep/turn-sleep-tracking-on/)

</div>

<div class="menu__item">

[Sleep
report](/Support/Product-support/suunto_7/suunto_7/sleep/sleep-report/)

</div>

<div class="menu__item">

[Cinema
mode](/Support/Product-support/suunto_7/suunto_7/sleep/cinema-mode/)

</div>

<div class="menu__item">

[Sleep insights in Suunto mobile
app](/Support/Product-support/suunto_7/suunto_7/sleep/sleep-insights-in-suunto-mobile-app/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Control music from your
wrist](/Support/Product-support/suunto_7/suunto_7/music/control-music-from-your-wrist/)

</div>

<div class="menu__item">

[Listen to music without your
phone](/Support/Product-support/suunto_7/suunto_7/music/listen-to-music-without-your-phone/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Maximize battery life in daily
use](/Support/Product-support/suunto_7/suunto_7/battery-life/maximize-battery-life-in-daily-use/)

</div>

<div class="menu__item">

[Maximize battery life during
exercise](/Support/Product-support/suunto_7/suunto_7/battery-life/maximize-battery-life-during-exercise/)

</div>

<div class="menu__item">

[Check battery life &
usage](/Support/Product-support/suunto_7/suunto_7/battery-life/check-battery-life--usage/)

</div>

</div>

<div class="menu__item">

[FAQ](/Support/Product-support/suunto_7/suunto_7/faq/)

</div>

<div class="menu__item">

[How to
videos](/Support/Product-support/suunto_7/suunto_7/how-to-videos/)

</div>

<div class="menu">

<div class="menu__item">

[Handling
guidelines](/Support/Product-support/suunto_7/suunto_7/care-and-support/handling-guidelines/)

</div>

<div class="menu__item">

[Disposal](/Support/Product-support/suunto_7/suunto_7/care-and-support/disposal/)

</div>

<div class="menu__item">

[Getting
support](/Support/Product-support/suunto_7/suunto_7/care-and-support/getting-support/)

</div>

</div>

<div class="menu__item">

[Glossary](/Support/Product-support/suunto_7/suunto_7/glossary/)

</div>

<div class="menu">

<div class="menu__item">

[Manufacturer's
info](/Support/Product-support/suunto_7/suunto_7/reference/manufacturers-info/)

</div>

<div class="menu__item">

[Compliance](/Support/Product-support/suunto_7/suunto_7/reference/compliance/)

</div>

<div class="menu__item">

[Trademark](/Support/Product-support/suunto_7/suunto_7/reference/trademark/)

</div>

<div class="menu__item">

[Patent
notice](/Support/Product-support/suunto_7/suunto_7/reference/patent-notice/)

</div>

<div class="menu__item">

[Copyright](/Support/Product-support/suunto_7/suunto_7/reference/copyright/)

</div>

<div class="menu__item">

[International Limited
Warranty](/Support/Product-support/suunto_7/suunto_7/reference/international-limited-warranty/)

</div>

</div>

<div class="menu">

<div class="menu__item">

[Types of safety
precautions](/Support/Product-support/suunto_7/suunto_7/safety/types-of-safety-precautions/)

</div>

<div class="menu__item">

[Safety
precautions](/Support/Product-support/suunto_7/suunto_7/safety/safety-precautions/)

</div>

</div>

</div>

<div class="select-element select-element--small select-element--sidebar m-t-md">

Bulgarian Chinese (Traditional) Dutch English Greek Tagalog Turkish

</div>

</div>

</div>

<div class="container-fluid wrapper manual-page__manual-content u-width-100 u-height-100 p-h-0 m-h-0 f-16 u-bg-white">

<div class="breadcrumb breadcrumb--top u-bg-white">

- [Start](/Support/Product-support/suunto_7/suunto_7/)
- [Daily
  activity](/Support/Product-support/suunto_7/suunto_7/activity-tracking/)

<!-- -->

- Daily activity

</div>

<div class="manual-page__content-area">

<div class="row u-bg-white m-0 u-relative">

<div class="col-xs-12">

<div class="manual-page__content-area-wrapper">

<div class="manual-page__content-area__content">

# Daily activity

In addition to sports tracking, you can use your
<span class="df-dynamic-context-title">Suunto 7</span> to keep track of
your daily activity and recovery. You can follow your daily steps,
calories, heart rate, body resources and sleep on your watch and follow
the trends with the Suunto mobile app.

[Steps](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/view-and-manage-your-tiles/#6.3)  
[Calories](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/view-and-manage-your-tiles/#6.3)  
[Daily heart
rate](/Support/Product-support/suunto_7/suunto_7/activity-tracking/daily-heart-rate/)  
[Body
resources](/Support/Product-support/suunto_7/suunto_7/activity-tracking/body-resources/)  
[Sleep](/Support/Product-support/suunto_7/suunto_7/sleep/)  
[Google
Fit](/Support/Product-support/suunto_7/suunto_7/wear-os-by-google/google-fit/)

</div>

<span class="suunto-icon suunto-icon-list-view f-24 m-r-xs"></span>
Table of Content

<div class="pagination pagination--no-page-numbers u-flex u-flex-justify-space-between">

<a
href="/Support/Product-support/suunto_7/suunto_7/heart-rate/follow-your-heart-rate-with-suunto-7/"
class="pagination__previous u-flex u-flex-valign-center"
rel="prev"><span
class="suunto-icon suunto-icon-arrow-long-left f-24"></span> <span
class="pagination__text m-l-sm f-bold f-14">Previous</span></a> <a
href="/Support/Product-support/suunto_7/suunto_7/activity-tracking/daily-heart-rate/"
class="pagination__next u-flex u-flex-valign-center" rel="next"><span
class="pagination__text m-r-sm f-bold f-14">Next</span> <span
class="suunto-icon suunto-icon-arrow-long-right f-24"></span></a>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="footer__social-networks container-fluid wrapper p-v-xxl">

Follow us

<a href="https://www.facebook.com/Suunto"
class="suunto-icon suunto-icon-facebook"
data-footer-some-link="Facebook" target="_blank"
rel="noreferrer nofollow" title="Facebook"></a>
<a href="https://instagram.com/suunto"
class="suunto-icon suunto-icon-instagram"
data-footer-some-link="Instagram" target="_blank"
rel="noreferrer nofollow" title="Instagram"></a>
<a href="https://www.youtube.com/suuntoTV"
class="suunto-icon suunto-icon-youtube" data-footer-some-link="Youtube"
target="_blank" rel="noreferrer nofollow" title="Youtube"></a>
<a href="https://www.tiktok.com/@suuntoglobal"
class="suunto-icon suunto-icon-tiktok" data-footer-some-link="TikTok"
target="_blank" rel="noreferrer nofollow" title="TikTok"><img
src="data:image/svg+xml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjQwIiBoZWlnaHQ9IjMyIiB2aWV3Ym94PSIwIDAgMzIgMzIiPgogICAgICAgICAgICAgICAgICAgIDxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZS1saW5lam9pbj0ibWl0ZXIiIHN0cm9rZS1saW5lY2FwPSJidXR0IiBzdHJva2UtbWl0ZXJsaW1pdD0iNCIgc3Ryb2tlLXdpZHRoPSIyIiBkPSJNMTYgMS4zMzNjOC4xIDAgMTQuNjY3IDYuNTY2IDE0LjY2NyAxNC42NjdzLTYuNTY2IDE0LjY2Ny0xNC42NjcgMTQuNjY3Yy04LjEgMC0xNC42NjctNi41NjYtMTQuNjY3LTE0LjY2N3M2LjU2Ni0xNC42NjcgMTQuNjY3LTE0LjY2N3oiIC8+CiAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIxLjcxNCA4LjVoLTExLjQyOGMtMC40NzMgMC0wLjkyOCAwLjE4OS0xLjI2MyAwLjUyNHMtMC41MjQgMC43ODktMC41MjQgMS4yNjN2MTEuNDI4YzAgMC40NzMgMC4xODkgMC45MjggMC41MjQgMS4yNjNzMC43ODkgMC41MjMgMS4yNjMgMC41MjNoMTEuNDI4YzAuNDczIDAgMC45MjgtMC4xODkgMS4yNjMtMC41MjNzMC41MjMtMC43ODkgMC41MjMtMS4yNjN2LTExLjQyOGMwLTAuNDczLTAuMTg5LTAuOTI4LTAuNTIzLTEuMjYzcy0wLjc4OS0wLjUyNC0xLjI2My0wLjUyNHpNMjAuMjg3IDE1LjA0NGMtMC4wNzkgMC4wMDgtMC4xNjUgMC4wMTItMC4yNDcgMC4wMTMtMC40NDUgMC0wLjg4Mi0wLjExMS0xLjI3My0wLjMyMnMtMC43MjMtMC41MTctMC45NjctMC44ODl2NC4xMmMwIDAuNjAyLTAuMTc4IDEuMTkxLTAuNTEzIDEuNjkycy0wLjgxIDAuODkxLTEuMzY2IDEuMTIyYy0wLjU1NiAwLjIzLTEuMTY5IDAuMjkxLTEuNzU5IDAuMTczcy0xLjEzNC0wLjQwOC0xLjU1OS0wLjgzM2MtMC40MjYtMC40MjYtMC43MTYtMC45NjgtMC44MzMtMS41NTlzLTAuMDU3LTEuMjAzIDAuMTczLTEuNzU5YzAuMjMtMC41NTYgMC42Mi0xLjAzMiAxLjEyMS0xLjM2NnMxLjA4OS0wLjUxMyAxLjY5Mi0wLjUxM2MwLjA2NCAwIDAuMTI2IDAuMDA1IDAuMTg4IDAuMDA5djEuNWMtMC4yMS0wLjAyNi0wLjQyMy0wLjAwOS0wLjYyNyAwLjA1MHMtMC4zOTIgMC4xNi0wLjU1NiAwLjI5NWMtMC4xNjMgMC4xMzUtMC4yOTcgMC4zMDMtMC4zOTIgMC40OTFzLTAuMTUxIDAuMzk1LTAuMTY0IDAuNjA3Yy0wLjAxMyAwLjIxMSAwLjAxOCAwLjQyMyAwLjA5MCAwLjYyMnMwLjE4NCAwLjM4MiAwLjMzIDAuNTM2IDAuMzIxIDAuMjc3IDAuNTE1IDAuMzYxYzAuMTk0IDAuMDg0IDAuNDA0IDAuMTI2IDAuNjE2IDAuMTI2IDAuNDE3IDAuMDA3IDAuODE5LTAuMTUxIDEuMTIxLTAuNDM3czAuNDgtMC42ODEgMC40OTUtMS4wOTdsMC4wMTUtNi45OTdoMS40MzZjMC4wNjYgMC42MjQgMC4zNDkgMS4yMDUgMC43OTkgMS42NDJzMS4wNDAgMC43MDEgMS42NjYgMC43NDZ2MS42Njh6IiAvPgogICAgICAgICAgICAgICAgPC9zdmc+" /></a>
<a href="/suunto-rss-feeds/" class="suunto-icon suunto-icon-rss"
data-footer-some-link="RSS Feed" target="_blank"
rel="noreferrer nofollow" title="RSS Feed"></a>

</div>

<div class="footer__links container-fluid wrapper">

<div class="row">

<div class="col-xs-12 col-lg-12">

<div class="row">

<div class="footer__links-container p-v-xl" v-if="!$mq.laptop">

- Country and language

- <div class="u-width-100">

  </div>

</div>

<div class="footer__links-container p-v-xl">

- Support
- <a
  href="/Support/Suunto-Webshop/faqsforsuuntowebshop/returns-and-refunds/"
  data-footer-support-link="">Returns and refunds</a>
- <a href="/Redirects/For-navigation/Contact-information/"
  data-footer-support-link="">Support main page</a>
- <a href="/Support/Software-updates/"
  data-footer-support-link="">Software updates</a>
- <a href="/Support/User-guides/" data-footer-support-link="">User
  guides</a>
- <a href="/Support/suunto-repair-center/"
  data-footer-support-link="">Suunto Repair Center</a>
- <a href="/Support/Service-Centers/suunto-service-centers/"
  data-footer-support-link="">Service Centers</a>
- <a href="/Redirects/For-navigation/Tutorial-Tuesday1/"
  data-footer-support-link="">Tutorial Tuesday</a>
- <a href="/Redirects/For-navigation/contact-us/"
  data-footer-support-link="">Contact us</a>

</div>

<div class="footer__links-container p-v-xl">

- Where to buy
- <a href="/Support/Suunto-Webshop/" data-footer-buy-link="">Suunto
  Webshop</a>
- <a href="/Support/Suunto-Webshop/faqsforsuuntowebshop/"
  data-footer-buy-link="">FAQs for Suunto Webshop</a>
- <a href="/suunto-pro-club/" data-footer-buy-link="">Suunto Pro Club</a>

</div>

<div class="footer__links-container p-v-xl">

- About Suunto
- <a href="/News/?category=news" data-footer-about-link="">News</a>
- <a href="/About-Suunto/Company-info/" data-footer-about-link="">Company
  info</a>
- <a href="/About-Suunto/Company-info/Careers/"
  data-footer-about-link="">Careers</a>
- <a href="/About-Suunto/heritage/" data-footer-about-link="">Heritage</a>
- <a href="/About-Suunto/Media/" data-footer-about-link="">Media</a>
- <a href="/About-Suunto/Sustainability/"
  data-footer-about-link="">Sustainability</a>
- <a href="/About-Suunto/eu-declarations-of-conformity/"
  data-footer-about-link="">EU Declarations of Conformity</a>
- <a href="/About-Suunto/whistleblowing/"
  data-footer-about-link="">Whistleblowing</a>

</div>

<div class="footer__links-container p-v-xl">

- Partners
- <a href="/partners/strava/" data-footer-partner-link="">Strava</a>
- <a href="/partners/trainingpeaks/"
  data-footer-partner-link="">TrainingPeaks</a>
- <a href="/partners/value-pack/" data-footer-partner-link="">Value
  Pack</a>
- <a href="/partners/welcome-partners/"
  data-footer-partner-link="">Welcome Partners</a>
- <a href="/partners/partners/" data-footer-partner-link="">Partners</a>

</div>

<div class="footer__links-container p-v-xl" v-if="$mq.laptop">

- Country and language

- <div class="u-width-100">

  </div>

</div>

</div>

</div>

</div>

</div>

<div class="footer__bottom-page container-fluid wrapper">

<div class="row">

<div class="col-xs-12 f-center">

<div class="f-uppercase f-12 f-center u-block">

<span class="u-inline-block">.</span>
<span class="u-inline-block">Copyright © 2025 Suunto.</span>
<span class="u-inline-block">All Rights Reserved. </span>

[Terms of use](/Terms-of-use/) \| [Privacy Policy](/Privacy-Policy/) \|
[SECURITY](/legal-pages/suunto-responsible-disclosure-policy/) \|
[Cookies](/legal-pages/cookies/) \|
<a href="#cookie-preference-center" id="ot-sdk-btn"
class="ot-sdk-show-settings cookie-preference-center">Cookie
Preferences</a> \| [\#YESsuunto terms](/legal-pages/yessuunto-terms/)

</div>

</div>

</div>

</div>

</div>
