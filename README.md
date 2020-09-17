# Tetration Python API Scripts #

The tetration API can be accessed by using Cisco's API package tetpyclient
https://pypi.org/project/tetpyclient/
```
pip install tetpyclient
```

## Tetration API Documentation ##
https://www.cisco.com/c/en/us/td/docs/security/workload_security/tetration-analytics/sw/config/b_Tetration_OpenAPI.html


## This environment can be setup in a docker container ##
### Build and run Docker Container ###
```
docker-compose build
docker-compose run --rm tet bash
```


## Notes ##
- The code/ folder is mounted into the docker container under /root/code
