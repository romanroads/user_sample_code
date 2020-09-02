@echo off
"C:\ProgramData\Miniconda3\condabin\conda.bat" env create -f environment_windows.yml && (
  echo Virtual Environment element is ready now && "C:\ProgramData\Miniconda3\condabin\conda.bat" activate element && python generate_gif.py --data_path "../" 
)



