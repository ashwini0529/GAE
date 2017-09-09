displayForm = """
<html>
	<body>
		<form method="POST" action="/display">
			<label>Please enter your name : </label> &nbsp;&nbsp;&nbsp;
			<input type="text" name="name">
			<input type="submit" value="Print Name">
		</form>
	</body>
</html>
"""

menu = """
<html>
	<body>
		<ul>
			<li><a href="/display">Display name</li>
		</ul>
	</body>
</html>
"""

calculatorForm = """
<html>
	<body>
		<form method="POST" action="/calculate">
			<label>Please enter number 1 : </label> &nbsp;&nbsp;&nbsp;
			<input type="text" name="num1"> <br><br>
			<label>Please enter number 2 : </label> &nbsp;&nbsp;&nbsp;
			<input type="text" name="num2"><br><br>
			<input type="radio" name="operation" value="+" checked> Add<br>
 			<input type="radio" name="operation" value="-"> Subtract<br>
  			<input type="radio" name="operation" value="*"> Multiply<br>
			<input type="radio" name="operation" value="/"> Divide<br><br>
  			&nbsp;&nbsp;&nbsp;
			<input type="submit" value="Calculate">
		</form>
	</body>
</html>
"""