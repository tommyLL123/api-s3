import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    ruta_archivo = event['body']['ruta_archivo'] 
    contenido = event['body']['contenido']
    
    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=ruta_archivo, Body=contenido)
    
    return {
        'statusCode': 200,
        'mensaje': f'Archivo {ruta_archivo} subido correctamente a {nombre_bucket}'
    }
