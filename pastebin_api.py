import requests

#this is the pastebin api
def make_pasty(title,contents,listing=1,expir='1M'):
    """
    Posts a new paste to linked user paste bin

    :param title: Paste Title
    :param contetnts: Paste Contents
    :param: listing: Whether listing is public(0),unlisted(1), or private(2)
    :param expir: How long the paste will be available for
    :returns URL of paste if successfull, otherwise error statement w/ context
    """

    print("creating the pastebin now")
    info={
    'api_dev_key': 'M49BOaqTC5cZSjDNXl3sfairtp9MhiXV',
    'api_user_key':'7bcfb01aef32303783150a38214b20ea',
    'api_option':'paste',
    'api_paste_name':title,
    'api_paste_code': contents,
    'api_paste_private':listing,
    'api_paste_expire_date':expir
    }
    url='https://pastebin.com/api/api_post.php'
    resp_msg=requests.post(url,data=info)
    if resp_msg.status_code==requests.codes.ok:
        print("paste created! Congrats!")
        return resp_msg.text
    else:
        print("Pastebin Error Code:",resp_msg.status_code," Reason: "+resp_msg.reason)












