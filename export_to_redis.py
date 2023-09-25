import redis
import xmltodict

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

# Read and parse the config.xml file
with open('config.xml', 'r') as xml_file:
    config_dict = xmltodict.parse(xml_file.read())

# Export subdomains to Redis
subdomains = config_dict['config']['subdomains']['subdomain']
redis_client.set('subdomains', str(subdomains))

# Export cookies to Redis
cookies = config_dict['config']['cookies']['cookie']
for cookie in cookies:
    name = cookie['@name']
    host = cookie['@host']
    value = cookie['#text']
    redis_key = f'cookie:{name}:{host}'
    redis_client.set(redis_key, value)

# Print keys saved to Redis
print("Keys saved to Redis:")
for key in redis_client.keys('*'):
    print(key, redis_client.get(key))
