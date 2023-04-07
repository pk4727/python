n=input("enter the no:-")
print(ord(n))
'''
Character	Character Name	ASCII code	 	Character	Character Name	ASCII code	 	Character	Character Name	ASCII code
!	Exclamation point	33	 	A	Uppercase a	65	 	a	Lowercase a	97
“	Double quotation	34	 	B	Uppercase b	66	 	b	Lowercase b	98
#	Number sign	        35	 	C	Uppercase c	67	 	c	Lowercase c	99
$	Dollar sign      	36	 	D	Uppercase d	68	 	d	Lowercase d	100
%	Percent sign	    37	 	E	Uppercase e	69	 	e	Lowercase e	101
&	ampersand	        38	 	F	Uppercase f	70	 	f	Lowercase f	102
‘	apostrophe       	39	 	G	Uppercase g	71	 	g	Lowercase g	103
(	Left parenthesis	40	 	H	Uppercase h	72	 	h	Lowercase h	104
)	Right parenthesis	41	 	I	Uppercase i	73	 	i	Lowercase i	105
*	asterisk	        42	 	J	Uppercase j	74	 	j	Lowercase j	106
+	Plus sign	        43	 	K	Uppercase k	75	 	k	Lowercase k	107
,	comma	            44	 	L	Uppercase l	76	 	l	Lowercase l	108
–	hyphen	            45	 	M	Uppercase m	77	 	m	Lowercase m	109
.	period          	46	 	N	Uppercase n	78	 	n	Lowercase n	110
/	slash           	47	 	O	Uppercase o	79	 	o	Lowercase o	111
0	zero	            48	 	P	Uppercase p	80	 	p	Lowercase p	112
1	one             	49	 	Q	Uppercase q	81	 	q	Lowercase q	113
2	two	                50	 	R	Uppercase r	82	 	r	Lowercase r	114
3	three	            51	 	S	uppercases	83	 	s	Lowercase s	115
4	four	            52	 	T	Uppercase t	84	 	t	Lowercase t	116
5	five	            53	 	U	Uppercase u	85	 	u	Lowercase u	117
6	six	                54	 	V	Uppercase v	86	 	v	Lowercase v	118
7	seven	            55	 	W	Uppercase w	87	 	w	Lowercase w	119
8	eight	            56	 	X	Uppercase x	88	 	x	Lowercase x	120
9	nine	            57	 	Y	Uppercase y	89	 	y	Lowercase y	121
:	colon	            58	 	Z	Uppercase z	90	 	z	Lowercase z	122
;	semi-colon      	59	 	[	Left square bracket 	91	 	{	Left curly brace	123
<	Less-than sign  	60	 	\	backslash	            92	 	|	Vertical bar	    124
=	Equals sign     	61	 	]	Right square bracket	93	 	}	Right curly brace	125
>	Greater-than sign	62	 	^	caret	                94	 	~	tilde           	126
?	Question mark	    63	 	_	underscore          	95	 	 	 	 
@	At sign	            64	 	`	Grave accent        	96	

	 	 	 
So what’s before 33 and beyond 126?
ASCII values before 32 (0-31) are control characters. A character code is often used in in-band signaling as a reference point in a set of characters to avoid adding additional symbols to the text.
At 32, we have space, it is included as printed characters, however, it’s not wrong to say space could also serve as a control character.
At 127, we have DEL (delete), which is a control character.
After 127, (128-255), we have Extended ASCII characters representing mathematical and other symbols that are not represented as keys and are not used in general.
Below are the ASCII values of control characters (0-31, 127):


Character	Character Name	ASCII Code	 	Character	Character Name	ASCII Code	 	Character	Character Name	ASCII Code
NULL    Null character	    00	 	VT	Vertical tab	    11	 	SYN	Synchronous idle	22
SOH	    Start of header 	01	 	FF	Form feed	        12	 	ETB	End of trans. Block	23
STX	    Start of text	    02	 	CR	Carriage return 	13	 	CAN	cancel	            24
ETX 	End of text	        03	 	SO	Shift out	        14	 	EM	End of medium	    25
EOT	    End of transmission	04	 	SI	Shift in	        15	 	SUB	substitute	        26
ENQ	    enquiry	            05	 	DLE	Data link escape	16	 	ESC	escape	            27
ACK	    acknowledge	        06	 	DC1	Device control 1	17	 	FS	File separator	    28
BEL	    bell	            07	 	DC2	Device control 2	18	 	GS	Group separator	    29
BS	    backspace	        08	 	DC3	Device control 3	19	 	RS	Record separator	30
HT	    Horizontal tab	    09	 	DC4	Device control 4	20	 	US	Unit separator	    31
LF	    Line feed	        10	 	NAK	Negative acknowledge21	 	DEL'''



