import calendar
import datetime

# დაწერეთ ფუნქცია lesser_of_two_evens, რომელსაც გადაეცემა 2 int ტიპის არგუმენტი.
# ○ გადაამოწმეთ არგუმენტების ტიპი, თუ რომელიმე არ იქნება int ტიპის, დააბრუნეთ None.
# ○ თუ ორივე არგუმენტი იქნება int ტიპის, ფუნქციამ უნდა დააბრუნოს მათ შორის
# უმცირესი, თუ ორივე არგუმენტი არის ლუწი. სხვა შემთხვევაში ფუნქციამ უნდა
# დააბრუნოს მათ შორის უდიდესი.


def lesser_of_two_evens(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        nums = [num1, num2]
        if num1 % 2 == 0 and num2 % 2 == 0:
            return max(nums)
        else:
            return min(nums)
    else:
        return None

# დაწერეთ ფუნქცია distance_from_zero, რომელსაც ექნება ერთი პარამეტრი. თუ
# გადაცემული არგუმენტის ტიპი იქნება int ან float, მაშინ დააბრუნეთ გადაცემული
# არგუმენტის აბსოლუტური მნიშვნელობა (მათემატიკური მოდული). სხვა შემთხვევაში
# დააბრუნეთ None.


def distance_from_zero(num):
    if isinstance(num, int) or isinstance(num, float):
        return abs(num)


""" დაწერეთ ფუნქცია bmi_calculator, 
რომელმაც უნდა გამოითვალოს არგუმენტების მიხედვით BMI ინდექსი.
თქვენ ფუნქციას უნდა ჰქონდეს 3 პარამეტრი: weight, height, metric. weight და height
პარამეტრები უნდა იყოს აუცილებელი (აუცილებლად უნდა გადაეცეს მნიშვნელობა), ხოლო
metric პარამეტრს უნდა ჰქონდეს ნაგულისხმევი მნიშვნელობა "m".
weight და height არგუმენტის ტიპები უნდა იყოს int ან float. ასევე არ შეიძლება ისინი
იყვნენ უარყოფითი რიცხვები. metric არგუმენტის ტიპი უნდა იყოს str და შესაძლებელია
ჰქონდეს 2 მნიშვნელობა: "m" (მეტრი) ან "cm" (სანტიმეტრი). თუ აქ ჩამოთვლილი
რომელიმე წესი დაირღვევა, ფუნქციამ უნდა დააბრუნოს None.
თუ ყველა გდამოცემული არგუმენტი იქნება სწორი ტიპის და ექნებათ სწორი მნიშვნელობა,
metric არგუმენტის მიხედვით გამოთვალეთ BMI ინდeქსი, დაამრგვალეთ მეათედებამდე და
დააბრუნეთ მიღებული შედეგი. ანუ თუ metric-ს ექნება "m" მნიშვნელობა, უნდა
გამოიყენოთ პირველი ფორმულა - მეტრებისთვის. ხოლო თუ ექნება "cm" მნიშვნელობა,
უნდა გამოიყენოთ მეორე ფორმულა - სანტიმეტრებისთვის."""


def bmi_calculator(weight, height, metric="m"):
    if metric == "cm" and isinstance(weight, int or float) and isinstance(height, int or float):
        bmi = weight / height / height * 10000
        return bmi
    elif metric == "m" and isinstance(weight, int or float) and isinstance(height, int or float):
        bmi = weight/height**2
        return bmi
    else:
        return None


""" დაწერეთ ფუნქცია print_date, რომელსაც ექნება 3 პარამეტრი: day, month, year. ფუნქციამ
უნდა დაბეჭდოს გადაცემული თარიღი day/month/year ფორმატით. თუმცა სანამ
დაბეჭდავს, მანამდე საჭიროა ვალიდაცია, ამიტომაც დაწერეთ ვალიდაციის ფუნქციები:
○ is_valid_year ფუნქცია, რომელსაც ექნება 1 პარამეტრი year და გადაამოწმებს
ვალიდურობას. ვალიდურია წელი თუ ის მეტია 0-ზე და ნაკლებია მიმდინარე
წელზე. მიმდინარე წელის გამოსათვლელად გამოიყენეთ პითონის ჩაშენებული
მოდულის datetime-ის datetime.today() კომპონენტი, რომელსაც აქვს year
ატრიბუტი. მაგალითის ნახვა, თუ როგორ მიწვდეთ მიმდინარე თარიღს, შეგიძლიათ
ამ ლინკზე. თუ გადაცემული არგუმენტი ამ ვალიდურობის წესს აკმაყოფილებს
დააბრუნეთ True, სხვა შემთხვევაში დააბრუნეთ False.
○ is_valid_month ფუნქცია, რომელსაც ექნება 1 პარამეტრი month. ვალიდურია თვე
თუ ის მოთავსებულია 1-სა და 12-ს შორის (1-იც და 12-იც შეიძლება იყოს). თუ
გადაცემული არგუმენტი ამ ვალიდურობის წესს აკმაყოფილებს დააბრუნეთ True,
სხვა შემთხვევაში დააბრუნეთ False.
○ is_valid_day ფუნქცია, რომელსაც ექნება 3 პარამეტრი: day, month, year.
იმისთვის, რომ დღე იყოს ვალიდური, ის მოთავსებული უნდ აიყოს 1-სა და თვის
შესაბამის მაქსიმალულ რიცხვს შორის (1-იც და თვეში დღეების მაქსიმალური
რაოდენობაც შესაძლებელია). იმისთვის, რომ კონკრეტული წლის კონკრეტული
თვის დღეების რაოდენობა გაიგოთ გამოიყენეთ პითონის ჩაშენებული მოდულის
calendar-ის monthrange ფუნქცია, რომელსაც არგუმენტად უნდა გადასცეთ წელი
და თვე და ის შედეგად დაგიბრუნებთ tuple-ს, რომელშიც პირველი ელემენტი არის
გადაცემული თვის პირველი დღე კვირის რომელი დღე იყო, თუმცა ეს არ
გჭირდებათ არაფერში. ხოლო მეორე ელემენტი არის დღეების რაოდენობა თვეში.
მისი გამოყენების მაგალითი შეგიძლიათ იხილოთ ამ ლინკზე პირველივე პასუხში.
თუ გადაცემული day არგუმენტი აკმაყოფილებს ამ წესს, დააბრუნეთ True, სხვა
შემთხვევაში დააბრუნეთ False.
ეს სამივე ფუნქცია გამოიძახეთ print_date ფუნქციაში და თუ გადაცემული სამივე
არგუმენტი იქნება ვალიდური მხოლოდ ამ შემთხვევაში დაბეჭდეთ day/month/year. სხვა
შემთხვევაში დაბეჭდეთ Error. Invalid Date.
"""


def print_data(day, month, year):
    if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
        def is_valid_year(year1):
            today = datetime.date.today().year
            if today > year1 > 0:
                return True
            else:
                return False

        def is_valid_month(month1):
            if 13 > month1 > 0:
                return True
            else:
                return False

        if is_valid_year(year) and is_valid_month(month):

            def is_valid_day(day1, month2, year2):
                monthramge = calendar.monthrange(month2, year2)
                if 0 < day1 < monthramge[1]:
                    return True
                else:
                    return False

            if is_valid_day(day, month, year):
                return f'{day}/{month}/{year}'
            else:
                return "Error.inavlid data."
        else:
            return "Error.inavlid data."
    else:
        return "Error.inavlid data."
