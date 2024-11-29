#!/bin/bash

# Obtener todos los IDs de los grupos de seguridad
GROUP_IDS=$(aws ec2 describe-security-groups --query 'SecurityGroups[*].GroupId' --output text)

# Iterar sobre cada ID de grupo de seguridad y agregar las reglas
for ID in $GROUP_IDS
do
  # Agregar regla para el puerto 8888 TCP
  aws ec2 authorize-security-group-ingress --group-id $ID --protocol tcp --port 8888 --cidr 0.0.0.0/0 > .temp
  
  # Agregar regla para el puerto 80 HTTP
  aws ec2 authorize-security-group-ingress --group-id $ID --protocol tcp --port 80 --cidr 0.0.0.0/0 > .temp
done


sudo yum update -y
sudo yum install jq -y
sudo yum install python3 python3-pip -y
python3 -m pip install urllib3==1.25.11

python3 -m pip install jupyterlab


jupyter lab --ip=0.0.0.0 --port=8888 --no-browser