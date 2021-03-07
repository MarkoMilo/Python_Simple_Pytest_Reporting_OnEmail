# main.py

import os
import send_mail_report


def main():
    if os.name == 'nt':  # if OS Windows
        os.system(
            'cmd /c pytest -vv -s --template=html1/index.html --report=reports//simple_test_report.html test_function.py')
        send_mail_report.send_mail()
    else:
        os.system(
            'pytest -vv -s --template=html1/index.html --report=reports//simple_test_report.html test_function.py')
        send_mail_report.send_mail()


if __name__ == "__main__":
    main()
