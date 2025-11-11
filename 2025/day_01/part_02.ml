open CCList
open CCIO
open Printf

let year = "2025"
let day = "01"

let lines year day file =
  let path = sprintf "%s/day_%s/%s" year day file in
  with_in path read_lines_l

let main () =
  let input_lines = lines year day "input.txt" in
  iter (fun line -> printf "%s\n" line) input_lines

let () = main ()
