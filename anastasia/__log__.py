
{'date': 'Wed Mar 24 2021 17:57:08.697 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 27
    main()
  module <module> line 25
    Associa(j = Jogo())
  module <module> line 21
    self.mito = self.Nome(self.cena)
  module <module> line 14
    self.nome = J.a(self.CELULA, x=400, y=50, w=100, h=50, cena=cena)
AttributeError: 'Nome' object has no attribute 'CELULA'
'''},
{'date': 'Wed Mar 24 2021 18:04:27.330 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 15
  self.nome = J.a(Associa.VAZIO, x=400, y=50, w=90, h=30, o=0.9, style={"font-size":"20px"} cena=cena)
                                                                                             ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Mar 24 2021 18:08:36.892 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 22
  self.mito = self.Nome(nome="mitocôndria"x=600, y=250, cena=self.cena)
                                           ^
SyntaxError: invalid syntax
'''},