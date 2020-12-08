# Gramatica ascendente

## Expresiones
        <expresion> ::= <datatype>
                | <expComp>
                | <expBool>

## Expresiones con tipos
        <datatype> ::=  <colName>
                | <literal>
                | <funcCall>
                | <datatype> '+' <datatype>
                | <datatype> '-' <datatype>
                | <datatype> '/' <datatype>
                | <datatype> '*' <datatype> 
                | <datatype> '%' <datatype>
                | <datatype> '^' <datatype>
                | <datatype> '||' <datatype>
                | <datatype> '&' <datatype>
                | <datatype> '|' <datatype>
                | <datatype> '#' <datatype>
                | <datatype> '~' <datatype>
                | <datatype> '>>' <datatype>
                | <datatype> '<<' <datatype>
                | '(' <datatype> ')'

## Expresiones de comparacion:
        <expComp> ::= <datatype> '<' <datatype>
                | <datatype> '>' <datatype>
                | <datatype> '>=' <datatype>
                | <datatype> '<=' <datatype>
                | <datatype> '=' <datatype>
                | <datatype> '!=' <datatype>
                | <datatype> '<>' <datatype>
                | <datatype> BETWEEN <datatype> AND <datatype>
                | <datatype> NOT BETWEEN <datatype> AND <datatype>
                | <datatype> BETWEEN SYMMETRIC <datatype> AND <datatype>
                | <datatype> IS DISTINCT FFROM <datatype>
                | <datatype> IS NOT DISTINCT FROM <datatype>
                | <datatype> IS NULL
                | <datatype> IS NOT NULL
                | <datatype> ISNULL
                | <datatype> NOTNULL
                | <datatype> IS TRUE
                | <datatype> IS NOT TRUE
                | <datatype> IS FALSE
                | <datatype> IS NOT FALSE
                | <datatype> IS UNKNOWN
                | <datatype> IS NOT UNKNOWN

        <boolean> ::= <expComp>
                | litBool

## Expresiones de subqueries
        <expSubq> ::= <datatype> '<'  <subqValues> '(' <selectStmt> ')'
                | <datatype> '>'  <subqValues> '(' <selectStmt> ')'
                | <datatype> '>=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '<=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '='  <subqValues> '(' <selectStmt> ')'
                | <datatype> '!=' <subqValues> '(' <selectStmt> ')'
                | <datatype> '<>' <subqValues> '(' <selectStmt> ')'
                | <datatype> BETWEEN <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> NOT BETWEEN <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> BETWEEN SYMMETRIC <datatype> AND <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS DISTINCT FFROM <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT DISTINCT FROM <datatype> <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NULL <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT NULL <subqValues> '(' <selectStmt> ')'
                | <datatype> ISNULL <subqValues> '(' <selectStmt> ')'
                | <datatype> NOTNULL <subqValues> '(' <selectStmt> ')'
                | <datatype> IS TRUE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT TRUE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS FALSE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT FALSE <subqValues> '(' <selectStmt> ')'
                | <datatype> IS UNKNOWN <subqValues> '(' <selectStmt> ')'
                | <datatype> IS NOT UNKNOWN <subqValues> '(' <selectStmt> ')'

        <subqValues> ::= ALL
                | ANY
                | SOME

## Expresiones booleanas:
        <boolean> ::= <expComp>
                | litBool
                | EXISTS '(' <selectStmt> ')'
                | <datatype> IN '(' <selectStmt> ')'
                | <datatype> NOT IN '(' <selectStmt> ')'
                | <expSubq>

        <expBool> ::= <expBool> AND <boolean>
                | <expBool> OR <boolean>
                | NOT <expBool>
                | <boolean>

## Literales:
        <literal> ::= litBool
                | litString
                | litNum
                | litChar

## Llamada a funcion:
        <funcCall> ::= funcMath '(' <paramList> ')'
                | funcBool '(' <paramList> ')'
                | funcTrig '(' <paramList> ')'

        <paramList> ::= <paramList> ',' <datatype>
                | <datatype>

# Statements

## Select
        <selectStmt> ::= SELECT <selectParams> FROM <tableExp> <joinList> <whereCl> <groupByCl> <orderByCl> <limitCl>
                | SELECT DISTINCT <selectParams> FROM <tableExp> <whereCl> <groupByCl>

        <selectParams> ::= '*'
                        | <selectList>

        <selectList> ::= <selectList> ',' <expresion> 
                | <expresion>

### From
        <tableExp> ::= <tableExp> ',' <fromBody>
                | <fromBody> 

        <colName> ::= id
                | id.id

        <fromBody> ::= <colName>
                | '(' <selectStmt> ')'

### Joins
        <joinList> ::= <joinList> <joinCl>
                | <joinCl>

        <joinCl> ::= <joinOpt> JOIN <colName> ON <expBool>
                | <joinOpt> JOIN <colName> USING '(' <nameList> ')'
                | NATURAL <joinOpt> JOIN <colName>
                |

        <nameList> ::= <nameList> ',' <colName>
                | <colName>

        <joinOpt> ::= INNER
                | LEFT 
                | LEFT OUTER
                | RIGHT
                | RIGHT OUTER
                | FULL
                | FULL OUTER

### Where
        <whereCl> ::= WHERE <expBool>
                | /*epsilon*/

### Group By
        <groupByCl> ::= GROUP BY <groupList> <havingCl>
                | 

        <groupList> ::=  <groupList> ',' <colName>
                | <groupElem>

        <havingCl> ::= HAVING <expBool>
                |

### Order By
        <orderByCl> ::= ORDER BY <orderList>

        <orderList> ::= <orderList> ',' <orderByElem>
                | <orderByElem>

        <orderByElem> ::= <colName> <orderOpts> <orderNull>

        <orderOpts> ::= ASC
                | DESC
                |

        <orderNull> ::= NULL FIRST
                | NULL LAST
                |

### Limit
        <limitCl> ::= number <offsetLimit>
                | ALL <offsetLimit>
                |

        <offsetLimit> ::= OFFSET number
                        |