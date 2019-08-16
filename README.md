[![Build Status](https://travis-ci.com/line/line-bot-pyconkr2019.svg?token=oioFqJsXLNtxovczS4Xj&branch=master)](https://travis-ci.com/line/line-bot-pyconkr2019)

## 소개
- '파이콘 한국 2019 도우미' LINE bot 입니다.
- 이 bot은 파이콘 한국 2019를 더욱 재미있게 즐기기 위해 LINE 개발자들에 의해 만들어졌으며 파이콘 한국의 공식 봇은 아닙니다.  

## 활용방법
* 화면 아래 QR코드로 LINE에서 친구 추가를 하거나, 웹페이지 [https://lin.ee/8u983aq](https://lin.ee/8u983aq) 로 접속할 수 있습니다.
* 파이콘 한국 2019 참석자들은 이 저장소에 Pull Request를 보내서 기능을 추가하고 bot을 더 재미있고 유익하게 만드는데 기여할 수 있습니다.
* 모든 Pull Request 및 봇 활용시 파이콘 한국 CoC와 이 저장소의 CoC를 지키는 것만 허용합니다. 또한 보안문제 등을 방지하기 위해서 Bot이 외부 API를 호출하는 것은 제한하고 있습니다.
* 이 bot은 **파이콘 한국 2019가 종료되면 일정 기간이 지난 후 삭제**됩니다.

## 로컬에서 실행해보기
* 이 저장소를 로컬에 저장한 뒤에 다음과 같이 실행해 볼 수 있습니다. 
```
> pip install -r requirements.txt
> flask run
```

## 기여하기
* Pull request 본문에는 contact을 위한 email을 수집하고 있습니다.
  * PR을 보내주신 분들께는 부스에서 작은 선물을 드립니다.
  * PR을 보내주신 분들중 선정하여 8월 18일 LINE 열린 점심에 초대합니다.
* 기여에 대한 더욱 자세한 내용은 [`CONTRIBUTING.md`](CONTRIBUTING.md) 을 확인해주세요. 

## 개발환경 및 제약사항
* Python 3를 기반으로 합니다. Python 2는 지원하지 않습니다.
* os, sys, eval 등 보안에 문제될 수 있는 코드는 거부될 수 있습니다.
* `skills` 폴더 이외에는 기본적으로 기여를 권장하지 않습니다.

## 행동규범(CoC): Code of Conduct 

본 저장소는 LINE과 파이콘 한국 모두의 영향을 받기 때문에 두 행동규범(CoC)을 모두 따라주실것을 권고드립니다. 

* [라인 오픈소스의 Code of Conduct](CONTRIBUTING.md)

* [파이콘 한국의 Code of Conduct](https://www.pycon.kr/coc)

## 라이선스

[Apache 2.0](LICENSE)



## LINE Bot 친구 추가하기

![LINE 친구추가](/assets/img/bot_qrcode.png)
