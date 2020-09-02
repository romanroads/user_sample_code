# User Sample Code

## Python users

### Windows Env Setup

- Install Conda 

    You can download conda at: https://docs.conda.io/en/latest/miniconda.html.
    We used conda 4.8.2 when setting up the tests

- Setup virtual environment for Python
    
    - We provide a script under user_sample_code/python folder 
    for setting up the necessary environment, either double click or
    run in Windows command prompt:
    
            setup_env_windows.cmd
            
        this assumes conda was installed to the default path.
            
    - Alternatively, if you want to manually setup the virtual environment, you can do
    , in anaconda prompt,
            
            conda create -f environment_windows.yml
    
- Execute sample code

    - Open an anaconda command prompt (search for "anaconda")
        we recommend using "Run as administrator" to launcher anaconda 
        prompt
    
    - Activate virtual environment in anaconda prompt by doing:
        
            conda activate element
    
    - Launch the Element software
    
        configure your training environment, settings in Element and 
        launch the training environment
    
    - Run the sample code now in anaconda prompt:
    
            cd user_sample_code/python
            python test_training.py
        
        this will read ego vehicle data from Element, and send testing decision sequence commands
        to Element. Ctl-C will terminate the python process.

### Linux Env Setup
    TBD