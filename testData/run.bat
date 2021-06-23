pytest -s -v -m "sanity" --html=./reports/report_c.html testCases/ --browser chrome
rem pytest -s -v -m "sanity" --html=./reports/report_f.html testCases/ --browser firefox
@pause
rem pytest -s -v -m "sanity and regression" --html=./reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity or regression" --html=./reports/report.html testCases/ --browser chrome
