#
# My Graph Library implementation in NX/Tcl
#
# Petar Petrov h11729352@s.wu.ac.at
#
# How to run: `tclsh gpl.tcl` or `tclkit gpl.tcl`
#


#
# Prerequisites
#

package require nx
package require tcltest

namespace eval ::Base {
    #
    # Begin of my implementation
    # ---------------%<------------------
    #
    nx::Class create Graph {
		:property {edges {} }
		:property {nodes {} }
	

		:public method add {a:required b:required} {
			set edge [::Base::Edge new -A $a -B $b]
			set sourceNode [$a getname]
			set targetNode [$b getname]
			set exists 0
			#Check for existing edge:
			foreach pair ${:edges} {
				set edgesource [[$pair getA] getname]
				set edgetarget [[$pair getB] getname]
				if {$sourceNode == $edgesource && $targetNode == $edgetarget } {
					set exists 1
					} else {
						if {$sourceNode == $edgetarget && $targetNode == $edgesource } {
							set exists 1
							}
						}
				}
			#Add new edge:
			if {0 == $exists } {
				lappend :edges $edge
                if {$a ni ${:nodes}  } {
                    lappend :nodes $a
                }
                    
                if {$b ni ${:nodes} } {
                    lappend :nodes $b
                }	
            return edge
			}
		}
		#Print
		:public method prettyprint {} {
			set output "graph G {\nnode\[label=\"\"];\n"
			foreach node ${:nodes} {
				foreach edge ${:edges} {
					if {[$edge getA] == $node} {
						set nextLine "[$node getname] -- [[$edge getB] getname];\n"
						set updated_string [string map {( "" ) ""} $nextLine]
						append output $updated_string
					}
					
				}
			}
			append output "}"
			return $output
		}
		
    }

			
			
		
	
	
	
	nx::Class create Edge {
		:property A:object,type=::Base::Node,required
		:property B:object,type=::Base::Node,required
		
		:public method getA {} {
			return ${:A}
		}
		:public method getB {} {
			return ${:B}
		}
	}
	
	nx::Class create Node {
		:property name:required
	  
		:public method getname {} {
			return "(${:name})"
		}
	}
	
}
    # (Pls. enter your code here.)
    
    # 
    # ---------------%<------------------
    # End of my implementation
    #





#
# Test suite
#

namespace eval ::Base::Test {
    namespace import ::tcltest::*
    #
    # Acceptance tests
    #
    test test-1 {} -body {
        nx::Class info instances ::Base::Graph
    } -result {::Base::Graph}
    test test-2 {} -body {
	nx::Class info instances ::Base::Edge
    } -result {::Base::Edge}
    test test-3 {} -body {
	nx::Class info instances ::Base::Node
    } -result {::Base::Node}
    test test-4 {} -constraints {[info commands ::Base::Graph] ne ""} -body {
	::Base::Graph info methods add
    } -result {add}
    
    #
    # Begin of my tests
    # See also http://www.tcl.tk/man/tcl/TclCmd/tcltest.htm
    # ---------------%<------------------

    # (Pls. enter your additional tests here.)
	
	#Test 1 - Exact number of edges and nodes:
	test test-5 {} -body {
		set n1 [::Base::Node create n1 -name "n1"]
		set n2 [::Base::Node create n2 -name "n2"]
		set n3 [::Base::Node create n3 -name "n3"]
		set n4 [::Base::Node create n4 -name "n4"]
		set n5 [::Base::Node create n5 -name "n5"]
		set n6 [::Base::Node create n6 -name "n6"]
		set n7 [::Base::Node create n7 -name "n7"]
		set n8 [::Base::Node create n8 -name "n8"]
		set g1 [::Base::Graph new]
		$g1 add $n1 $n2
		$g1 add $n1 $n3
		$g1 add $n1 $n4
		$g1 add $n1 $n5
		$g1 add $n5 $n6
		$g1 add $n5 $n7
		$g1 add $n5 $n8
		set nredges [llength [$g1 cget -edges] ]
		set nrnodes [llength [$g1 cget -nodes] ]
		set final [list $nredges $nrnodes]
	} -result {7 8}
	
	
	#Test 2 - Pretty print graph:
	test test-6 {} -body {
		set n1 [::Base::Node create n1 -name "n1"]
		set n2 [::Base::Node create n2 -name "n2"]
		set n3 [::Base::Node create n3 -name "n3"]
		set n4 [::Base::Node create n4 -name "n4"]
		set n5 [::Base::Node create n5 -name "n5"]
		set n6 [::Base::Node create n6 -name "n6"]
		set n7 [::Base::Node create n7 -name "n7"]
		set n8 [::Base::Node create n8 -name "n8"]
		set g1 [::Base::Graph new]
		$g1 add $n1 $n2
		$g1 add $n1 $n3
		$g1 add $n1 $n4
		$g1 add $n1 $n5
		$g1 add $n5 $n6
		$g1 add $n5 $n7
		$g1 add $n5 $n8
		puts [$g1 prettyprint]
	} -result {}
	
	#Test 3 - Compare with required output:
	test test-7 {} -body {
		set n1 [::Base::Node create n1 -name "n1"]
		set n2 [::Base::Node create n2 -name "n2"]
		set n3 [::Base::Node create n3 -name "n3"]
		set n4 [::Base::Node create n4 -name "n4"]
		set n5 [::Base::Node create n5 -name "n5"]
		set n6 [::Base::Node create n6 -name "n6"]
		set n7 [::Base::Node create n7 -name "n7"]
		set n8 [::Base::Node create n8 -name "n8"]
		set g1 [::Base::Graph new]
		$g1 add $n1 $n2
		$g1 add $n1 $n3
		$g1 add $n1 $n4
		$g1 add $n1 $n5
		$g1 add $n5 $n6
		$g1 add $n5 $n7
		$g1 add $n5 $n8
		set result [$g1 prettyprint]
	} -result "graph G {\nnode\[label=\"\"\];\nn1 -- n2;\nn1 -- n3;\nn1 -- n4;\nn1 -- n5;\nn5 -- n6;\nn5 -- n7;\nn5 -- n8;\n}"
	
	
    
    # ---------------%<------------------
    # End of my tests
    #    
    cleanupTests
}
namespace delete ::Base::Test
