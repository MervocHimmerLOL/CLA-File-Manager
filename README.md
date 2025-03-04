CLA File Manager
Что из себя представляет данная программа? Простой файловый менеджер работающий из консоли. 
Как запустить? Три варианта:
1. python fmanager.py (Из папки с файлом)
2. ./fman.bat (Из папки с файлом)
3. Добавить папку с файлом в PATH и fman.bat откуда хотите.
4. Запустить ui.py, в качестве приятного бонуса - пользовательский интерфейс 

Функционал:
1. copy - принимает файл, и создает его коипю. Пример вызова python fmanager.py file.txt | ./fman.bat filt.txt | fman.bat <путь к файлу> (Если файл в одной папке с скриптом, то достаточно имени файла, иначе - полный путь к файлу)
2. delete - принимает файл/путь к нему, и удаляет его. Пример вызова - python fmanager.py delete file.txt | ./fman.bat delete file.txt | fman.bat <путь к файлу>
3. count - принимает путь к папке, подсчитывает количество фалов в ней. Пример вызова - python fmanager.py count C:\Users\user\PycharmProjects\CML-File-Manager | ./fman.bat <путь к папке> | fman.bat <путь к папке>
4. search - принимает паттерн(регулярное выражение) и ищет рекурсивно совпадения в папке(по умолчанию - папка со скриптом). Пример вызова - python fmanager.py search test | ./fman.bat search test -d <путь где искать> | fman.bat search --dir test (Расположение флага-d и паттерна не важно)
5. date - принимает файл/папку/папку и флаг -r и датирует файл/файлы в папке/файлы в папке и папках внутри папки. Примеры вызова - python fmanager.py date test.txt | ./fman.bat date C:\Users\user\PycharmProjects\CML-File-Manager | fman.bat date C:\Users\user\PycharmProjects\CML-File-Manager -r
6. analyze - принимает путь, и анализирует, сколько весит каждый файл, и вложенные в исходную папки. Пример вызова - python fmanager.py analyze C:\Users\user\PycharmProjects\CML-File-Manager | ./fman.bat analyze C:\Users\user\PycharmProjects\CML-File-Manager | fman.bat analyze C:\Users\user\PycharmProjects\CML-File-Manager
