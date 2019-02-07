import datetime
from decimal import *

correctanswers = ["" for i in range(0, 11)]

correctanswers[0] = [('ATL','Atlanta             '),('BOS','Boston              '),('ORD','Chicago             '),('DFW','Dallas-Fort Worth   '),('DEN','Denver              '),('FLL','Fort Lauderdale     '),('LAX','Los Angeles         '),('JFK','New York            '),('OAK','Oakland             '),('IAD','Washington          ')]

correctanswers[1] = [('Charles Brown                 ',), ('Charles Garcia                ',), ('Charles Gonzalez              ',), ('Charles Hall                  ',), ('Christopher Davis             ',)]

correctanswers[2] = [('cust5     ', 'Anthony Harris                ', datetime.date(1991, 3, 15), 'UA'),('cust66    ', 'Donna Allen                   ', datetime.date(1994, 3, 18), 'UA'),('cust98    ', 'George Collins                ', datetime.date(1995, 3, 7), 'UA')]

correctanswers[3] =[('Barbara Collins               ', 9L), ('Betty Edwards                 ', 9L), ('Carol Evans                   ', 9L), ('Charles Evans                 ', 9L), ('Anthony Allen                 ', 8L), ('Anthony Evans                 ', 8L), ('Anthony Garcia                ', 8L), ('Anthony Gonzalez              ', 8L), ('Barbara Davis                 ', 8L), ('Barbara Harris                ', 8L)]

correctanswers[4] = [('Anthony Allen                 ',),('Anthony Gonzalez              ',),('Barbara Davis                 ',),('Barbara Harris                ',),('Betty Baker                   ',),('Betty Jackson                 ',),('Brian Garcia                  ',),('Brian Jackson                 ',),('Carol Anderson                ',),('Carol Campbell                ',),('Carol Evans                   ',),('Charles Evans                 ',),('Charles Garcia                ',),('Charles Hall                  ',),('Daniel Brown                  ',),('Daniel Green                  ',),('Daniel Hernandez              ',),('Daniel Jackson                ',),('David Adams                   ',),('David Baker                   ',),('David Campbell                ',),('David Carter                  ',),('Donald Campbell               ',),('Donald Carter                 ',),('Donald Evans                  ',),('Donna Hall                    ',),('Dorothy Allen                 ',),('Dorothy Carter                ',),('Dorothy Edwards               ',),('Edward Brown                  ',),('Edward Carter                 ',),('Edward Garcia                 ',),('Edward Harris                 ',),('Elizabeth Jackson             ',),('George Brown                  ',),('George Garcia                 ',),('Helen Adams                   ',),('Helen Edwards                 ',),('Helen Hernandez               ',),('James Adams                   ',),('James Hall                    ',),('Jeff Baker                    ',),('Jeff Clark                    ',),('Jeff Green                    ',)]

correctanswers[5] = [('Barbara Davis                 ',),('Barbara Harris                ',),('Brian Garcia                  ',),('Daniel Green                  ',),('Daniel Jackson                ',),('David Adams                   ',),('Donald Allen                  ',),('George Garcia                 ',)]

correctanswers[6] = [('Metropolitan Oakland International                                                                  ', Decimal('0.84')), ('John F Kennedy International                                                                        ', Decimal('0.67')), ('General Edward Lawrence Logan International                                                         ', Decimal('0.60')), ('Washington Dulles International                                                                     ', Decimal('0.57')), ('Dallas Fort Worth International                                                                     ', Decimal('0.54')), ("Chicago O'Hare International                                                                        ", Decimal('0.50')), ('Fort Lauderdale Hollywood International                                                             ', Decimal('0.44')), ('Hartsfield Jackson Atlanta International                                                            ', Decimal('0.43')), ('Denver International                                                                                ', Decimal('0.40'))]

correctanswers[7] = [('Anthony Garcia                ',),('Barbara Collins               ',),('Betty Carter                  ',),('Betty Edwards                 ',),('Brian Jackson                 ',),('Carol Clark                   ',),('Carol Evans                   ',),('Carol Hall                    ',),('Charles Brown                 ',),('Charles Evans                 ',),('Charles Gonzalez              ',),('Charles Hall                  ',),('Christopher Hill              ',),('David Campbell                ',),('David Carter                  ',),('David Hernandez               ',),('Deborah Anderson              ',),('Deborah Baker                 ',),('Donald Campbell               ',),('Donna Edwards                 ',),('Dorothy Allen                 ',),('Edward Edwards                ',),('Elizabeth Anderson            ',),('Elizabeth Collins             ',),('Elizabeth Harris              ',),('Helen Allen                   ',),('Helen Edwards                 ',),('Helen Evans                   ',),('James Carter                  ',),('James Evans                   ',),('James Hall                    ',),('Jason Hernandez               ',),('Jeff Anderson                 ',)]

correctanswers[8] = [('Elizabeth Hall                ', datetime.date(2016, 8, 7), datetime.date(2016, 8, 9)),('Jeff Harris                   ', datetime.date(2016, 8, 2), datetime.date(2016, 8, 4))]

correctanswers[9] = [('SW110 ', 'SW171 ', 'DFW', 'DFW', datetime.timedelta(0, 3840)),('SW136 ', 'SW157 ', 'OAK', 'FLL', datetime.timedelta(0, 4740)),('AA114 ', 'SW171 ', 'DFW', 'DFW', datetime.timedelta(0, 6060)),('SW118 ', 'AA167 ', 'OAK', 'DFW', datetime.timedelta(0, 7200)),('SW118 ', 'UA128 ', 'OAK', 'FLL', datetime.timedelta(0, 7380))]

correctanswers[10] =[('Christopher Hernandez         ', 1L), ('Edward Evans                  ', 2L), ('Deborah Collins               ', 3L), ('George Davis                  ', 3L), ('Brian Evans                   ', 3L), ('Anthony Edwards               ', 3L), ('Donald Allen                  ', 7L), ('Charles Collins               ', 8L), ('Betty Gonzalez                ', 9L), ('David Garcia                  ', 10L), ('Carol Baker                   ', 10L), ('Betty Brown                   ', 10L), ('Daniel Baker                  ', 10L), ('Charles Garcia                ', 14L), ('Anthony Harris                ', 14L), ('David Hall                    ', 16L), ('David Hill                    ', 16L), ('Edward Brown                  ', 18L), ('Dorothy Edwards               ', 19L), ('Donna Hall                    ', 19L), ('Barbara Hall                  ', 19L), ('George Evans                  ', 19L), ('Helen Hernandez               ', 19L), ('Donald Adams                  ', 19L)]
