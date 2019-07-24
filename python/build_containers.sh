fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:2.5 --out packages-2.5 python2.5
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:2.6 --out packages-2.6 python2.6
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:2.7 --out packages-2.7 python2.7
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.2 --out packages-3.2 python3.2
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.3 --out packages-3.3 python3.3
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.4 --out packages-3.4 python3.4
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.5 --out packages-3.5 python3.5
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.6 --out packages-3.6 python3.6
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.7 --out packages-3.7 python3.7
rm -rf extracted
fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:3.8 --out packages-3.8 python3.8
rm -rf extracted
