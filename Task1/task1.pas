program task1;
var
	numbers: array of Integer;
	len: integer;

procedure print(text: string);
var 
	i:integer;
begin
	writeln(text);
	for i := 0 to High(numbers) do
		begin
			write(numbers[i], ' ');
		end;
		writeln();
end;

procedure generate_random_list(first: integer; last: integer; how_many: integer);
var
	i:integer;
begin
	len := how_many;
	Randomize;
	SetLength(numbers, how_many);
	for i := 0 to how_many - 1 do
		begin
			numbers[i] := Random(last - first + 1) + first;
		end;
end;

procedure bubble_sort();
var
	temp: integer;
	if_to_continue: boolean;
	i: integer;
begin
	if_to_continue := True;
	while if_to_continue do
		begin
		if_to_continue := False;
		for i := 0 to len - 2 do
			begin
				if numbers[i] > numbers[i+1] then
				begin
					temp := numbers[i+1];
					numbers[i+1] := numbers[i];
					numbers[i] := temp;
					if_to_continue := True;
				end;
			end;
		end;
end;

begin
	generate_random_list(0, 100, 10);
	print('Random numbers');
	bubble_sort();
	print('After bubble sort:')
end.

