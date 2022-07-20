import boto3
# 下記は使用しなくなるためコメントアウト
# import pprint

# import時に実行されないように関数化しておく
# また、textは引数で受け取れるように変更する
def translate(text):
	translate = boto3.client('translate')
	# text = 'あとでメールを送ります。'
	result = translate.translate_text(
	    Text=text, SourceLanguageCode='ja', TargetLanguageCode='en')

	# コンソールに表示せず、戻り値とするためコメントアウト
	# pprint.pprint(result)
	
	
	return result
