import twint

c = twint.Config()
c.Search = "Tesla"
twint.run.Search(c)