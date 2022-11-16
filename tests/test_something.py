import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User

# #
# resp = requests.get(SERVICE_URL)
# print(resp.__getstate__())
# print(resp.url)


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(200).validate(User)




#
# z = {"meta": {"pagination": {"total": 2542, "pages": 255, "page": 1, "limit": 10,
#                          "links": {"previous": None, "current": "https://gorest.co.in/public/v1/users?page=1",
#                                    "next": "https://gorest.co.in/public/v1/users?page=2"}}}, "data": [
#     {"id": 2596, "name": "Devdan Kaul", "email": "kaul_devdan@schowalter-johnson.org", "gender": "female",
#      "status": "active"},
#     {"id": 2595, "name": "Adityanandan Shukla", "email": "shukla_adityanandan@paucek.io", "gender": "male",
#      "status": "inactive"},
#     {"id": 2594, "name": "Ganaka Mukhopadhyay", "email": "mukhopadhyay_ganaka@johnston.net", "gender": "female",
#      "status": "inactive"},
#     {"id": 2593, "name": "Deeptimoyee Mishra JD", "email": "mishra_jd_deeptimoyee@price.info", "gender": "female",
#      "status": "active"},
#     {"id": 2592, "name": "Deevakar Varman", "email": "deevakar_varman@bogisich.biz", "gender": "female",
#      "status": "active"},
#     {"id": 2591, "name": "Dhara Desai DVM", "email": "desai_dhara_dvm@kuhlman.co", "gender": "male",
#      "status": "active"},
#     {"id": 2588, "name": "Acaryatanaya Agarwal", "email": "agarwal_acaryatanaya@oberbrunner-ratke.com",
#      "gender": "male", "status": "inactive"},
#     {"id": 2587, "name": "Rep. Anjali Pilla", "email": "pilla_anjali_rep@veum-spencer.net", "gender": "male",
#      "status": "inactive"},
#     {"id": 2586, "name": "Ekaksh Singh", "email": "singh_ekaksh@koch.info", "gender": "male", "status": "inactive"},
#     {"id": 2585, "name": "Pres. Charak Bhattacharya", "email": "bhattacharya_charak_pres@feest.co", "gender": "male",
#      "status": "active"}]}
