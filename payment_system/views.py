from django.shortcuts import redirect
from sslcommerz_lib import SSLCOMMERZ 
import random, string

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def payment(request):
    settings = { 'store_id': 'phitr671e3dcf89e2c', 'store_pass': 'phitr671e3dcf89e2c@ssl', 'issandbox': True }
        
    sslcz = SSLCOMMERZ(settings)
    
    post_body = {}
    post_body['total_amount'] = 100.12 
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator(),
    post_body['success_url'] = ""
    post_body['fail_url'] = ""
    post_body['cancel_url'] = ""
    post_body['emi_option'] = 0
    post_body['cus_name'] =  "request user username"
    post_body['cus_email'] = "request user email"
    post_body['cus_phone'] = "01700000000"
    post_body['cus_add1'] = "Cantonment" 
    post_body['cus_city'] = "Dhaka" 
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Flower title"
    post_body['product_category'] = "Flower category"
    post_body['product_profile'] = "general"

    response = sslcz.createSession(post_body) 
    print(response)
    
    return redirect(response['GatewayPageURL'])