# Gramatica ascendente

## Expresiones
    <datatype> ::= 
            | id
            | id.id
            | <literal>
            | <funcCall>
            | <datatype> '+' <datatype>
            | <datatype> '-' <datatype>
            | <datatype> '/' <datatype>
            | <datatype> '*' <datatype> 
            | <datatype> '%' <datatype>
            | <datatype> '^' <datatype>
            | '(' <datatype> ')'

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

    


