#!/usr/local/rvm/rubies/ruby-1.9.3-p194/bin/ruby

require './common/http_connector.rb'

format=ARGV[0]

ACCESS_KEY = 'PUDDING_TO_KEY'
url = 'http://openapi.pudding.to/api/v1/photos/popular'

if(format!=nil)
	url += ".#{format}"
end

headers = {
	"User-Agent" => "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
	"Accept" => "text/html,application/xhtml+xml,application/xml,application/json;q=0.9,*/*;q=0.8"
}

# request with GET method
#
#response, url = HttpConnector.get(url+"?access_key=#{ACCESS_KEY}", :headers => headers)

# request with POST method
#
response, ret_url = HttpConnector.post(url, :parameters=>{:access_key=>ACCESS_KEY}, :headers => headers)

puts 'response.code=' + response.code
puts 'response.msg=' + response.msg
puts 'response.body=' + response.body
