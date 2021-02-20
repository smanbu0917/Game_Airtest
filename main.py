import pytest

if __name__ == '__main__':
    pytest.main(["--html=Outputs/Reports/report.html",
                 "--alluredir=Outputs/allureDir"])
    # pytest.main()