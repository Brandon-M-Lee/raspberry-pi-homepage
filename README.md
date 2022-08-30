# raspberry-pi-homepage

## 가상 환경의 설치

Python 3.9.6을 사용하여라.

virtualenv가 설치되어 있지 않다면 다음 명령으로 virtualenv를 설치한다.

    pip install virtualenv

다음 명령으로 새로운 가상 환경을 생성한다. (최초 1회)

    virtualenv kndlkr

다음 명령으로 가상환경을 실행한다.
    
    ./kndlkr/Scripts/activate

또는

    ./kndlkr/Scripts/activate.bat

또는

    ./kndlkr/Scripts/activate.ps1

PowerShell에서 실행 정책 오류가 걸린다면 다음 명령으로 정책을 완화한 후 다시 실행한다.

    Set-ExecutionPolicy Unrestricted -Scope Process

다음 명령으로 가상 환경을 종료할 수 있다.

    deactivate

가상 환경 실행은 터미널을 열 때마다 다시 해야 한다.

## 가상 환경에 접속한 후
이 단락에서는 activate 프로그램을 실행시켜서 터미널의 가장 왼쪽에 (kndlkr)이 표시되는 상태에서 실행시켜야 한다.

다음 명령으로 요구되는 패키지들을 설치할 수 있다.

    pip install -r requirements.txt

다음 명령으로 프로그램을 실행시킨다.

    python app.py
