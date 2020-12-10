<p align="center">
  <img src="artifacts/ROMAN_ROADS_LOGO_COLOR.png" width="500" title="ROMAN ROADS, INC.">
</p>

# User Sample Code
This repo provides sample code, scripts that can be used to set up a typical Reinforcement Learning (RL),
Imitation Learning (IL) training environment, where the user algorithm is trained against real human
driving behaviors provided by Element Platform ([Element Client Archive Download](https://www.romanroads.io/element-archive/))

## Setup for Python users

### Windows 10 OS

- Install Conda 

    You can download conda at: https://docs.conda.io/en/latest/miniconda.html
    
    conda version > 4.8.2

- Create Python virtual environment
    
    - We provide a script under user_sample_code/python folder 
    for setting up the necessary environment, either double click or
    run in Windows command prompt:
    
            setup_env_windows.cmd
            
        this assumes conda was installed to the default path C:\ProgramData\Miniconda3\
            
    - Alternatively, if you want to manually setup the virtual environment, you can do
    , in anaconda prompt,
            
            conda create -f environment_windows.yml
    
- Launch the sample code as well as Element

    - Launch an anaconda command prompt (type "anaconda" in your Windows 10 search box)
        we recommend using "Run as administrator" to launcher anaconda 
        prompt
    
    - Activate virtual environment in anaconda prompt by doing:
        
            conda activate element
    
    - Launch the Element software
    
        configure your training environment, settings in Element and 
        launch the training environment
    
    - Run the sample code now in anaconda prompt:
    
            cd user_sample_code/python
            python test_read_write.py
        
        this will read ego vehicle data from Element, and send test decision sequence commands
        to Element which request for a left lane-change. The decision sequence and the traffic configuration are shown below:
        
<p align="center">
  <img src="artifacts/LeftLaneChange.png" width="500" title="ROMAN ROADS, INC.">
</p>

<p align="center">
  <img src="artifacts/LeftLaneChangeScene.png" width="500" title="ROMAN ROADS, INC.">
</p>
        
            cd user_sample_code/python
            python test_training.py
            
         this will set up a typical Reinforcement Learning environment which inherits from OpenAI Gym
         environments. Users can build up their own policy learning / updating algorithms thereafter. You need
         to select sample data "Exp22Run6Trip1" for this demo script which select Agent with ID 1854 as "human demonstrator"

### Linux
    TBD

### Mac OS
    TBD
