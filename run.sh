#!/bin/bash

declare -x dir_root=$(pwd)
declare -x file_src="insight_draft.py"
declare -x file_src=${dir_root}/src/${file_src}


python3 ${file_src}
