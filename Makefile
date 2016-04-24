store=store

blogs=meituan taobao


all: $(blogs)

taobao:
	@mkdir -p ./$(store)
	@rm -rf $(store)/taobao_items.json
	scrapy crawl taobao -o $(store)/taobao_items.json -t json

meituan:
	@mkdir -p ./$(store)
	@rm -rf $(store)/meituan_items.json
	scrapy crawl meituan -o $(store)/meituan_items.json -t json 

clean:
	rm -rf $(store) 
	find ./ -name "*.pyc" -exec rm -rf {} \;
