#install.bat
IDF_PATH=C:/esp/esp-idf
#export.bat

cd C:/esp/esp-idf/SK/eeprom
python C:/esp/esp-idf/tools/idf.py fullclean
python C:/esp/esp-idf/tools/idf.py  menuconfig
python C:/esp/esp-idf/tools/idf.py build
python C:/esp/esp-idf/tools/idf.py flash monitor  


cd C:/esp/esp-idf/SK/SKSL_Common

python C:/esp/esp-idf/tools/idf.py fullclean
python C:/esp/esp-idf/tools/idf.py  menuconfig
python C:/esp/esp-idf/tools/idf.py build
python C:/esp/esp-idf/tools/idf.py flash monitor  



