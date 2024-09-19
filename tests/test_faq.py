import pytest
import allure
from pages.home_page import YaScooterHomePage
from utils.data import YaScooterHomePageFAQ
from utils.locators import YaScooterHomePageLocator


class TestYaScooterFAQPage:
    @allure.title('При нажатии на вопрос отображается ответ')
    @allure.description(
        """
        Проверка, что при нажатии на поле вопроса в блоке с ответами на вопросы
        данный вопрос раскрывается и текст в нем соответствует обозначенному
        """
    )
    @pytest.mark.parametrize(
        'question, answer, expected_answer',
        [
            (0, 0, YaScooterHomePageFAQ.first),
            (1, 1, YaScooterHomePageFAQ.second),
            (2, 2, YaScooterHomePageFAQ.third),
            (3, 3, YaScooterHomePageFAQ.fourth),
            (4, 4, YaScooterHomePageFAQ.fifth),
            (5, 5, YaScooterHomePageFAQ.sixth),
            (6, 6, YaScooterHomePageFAQ.seventh),
            (7, 7, YaScooterHomePageFAQ.eighth),
        ]
    )
    def test_faq_click_first_question_show_answer(
        self, 
        driver, 
        question: int, 
        answer: int, 
        expected_answer: str
    ):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=question)
        answer = ya_scooter_home_page.find_element(YaScooterHomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert (
            answer.is_displayed() and answer.text == expected_answer, 
            'Ответ на вопрос не совпадает с ожидаемым значением '
        )
        