from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(@class,'AppHeader_header__linkText')and text()='Личный Кабинет']")        # Кнопка перехода в личный кабинет
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")                                                   # Кнопка входа в аккаунт
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")                                                          # Кнопка оформления заказа
    
class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/../input")                # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")             # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")                 # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")    # Кнопка регистрации 
    LOGIN_LINK = (By.XPATH, "//a[contains(@class,'Auth_link') and (text())='Войти']")  # Ссылка на страницу входа
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']")          # Сообщение об ошибке ввода
    

class AuthPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/../input")              # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/../input")          # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")                     # Кнопка входа
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")                      # Ссылка на страницу регистрации
    RECOVER_LINK = (By.XPATH, "//a[contains(@class,'Auth_link') and (text())='Восстановить пароль']")                          # Ссылка на восстановление пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")     # Ссылка на профиль пользователя
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li/a[@href='/']")           # Кнопка перехода к конструктору
    LOGO_LINK = (By.XPATH, "//div/a[@href='/']")                   # Ссылка-логотип на главную страницу
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")           # Кнопка выхода из аккаунта


class RecoveryPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(@class,'Auth_link') and (text())='Войти']")                # Ссылка на страницу входа с восстановления пароля


class BurgerIngredientLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")                                   # Кнопка переключения на вкладку "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")                                 # Кнопка переключения на вкладку "Соусы"
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']")                             # Кнопка переключения на вкладку "Начинки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")                                 # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")                               # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")                           # Раздел "Булки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span")   # Активная вкладка