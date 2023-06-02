package main

import (
	"fmt"
	"github.com/schwarmco/go-cartesian-product"
	"math"
)

var n byte
var nofSteps = make(map[string]int)

func getAllConfigurations() [][]byte {
	values := make([]interface{}, n+1)
	for i := range values {
		values[i] = i
	}
	duplicateValues := make([][]interface{}, n)
	for i := range duplicateValues {
		duplicateValues[i] = values
	}
	cart := cartesian.Iter(duplicateValues...)

	nofConfigurations := int(math.Pow(float64(n+1), float64(n)))
	//fmt.Println("nofConfigurations", nofConfigurations)
	configurations := make([][]byte, nofConfigurations)
	index := 0
	for c := range cart {
		configuration := make([]byte, len(c))
		for i, value := range c {
			temp := value.(int)
			configuration[i] = byte(temp)
		}
		configurations[index] = configuration
		index++
	}

	return configurations
}

func getProcessesInCriticalSec(c []byte) []byte {
	var processesInCriticalSec []byte

	// P0 has access to critical section
	if c[0] == c[n-1] {
		processesInCriticalSec = append(processesInCriticalSec, 0)
	}
	for i := byte(1); i <= n-1; i++ {
		// if Pi has access to critical section
		if c[i] != c[i-1] {
			processesInCriticalSec = append(processesInCriticalSec, i)
		}
	}
	return processesInCriticalSec
}

func nofStepsToSafeConf(c []byte) int {
	if s, ok := nofSteps[string(c)]; ok {
		return s
	} else {
		steps := 0
		processesInCS := getProcessesInCriticalSec(c)

		// c is not safe configuration
		if len(processesInCS) > 1 {
			for _, p := range processesInCS {
				copyOfC := make([]byte, n)
				copy(copyOfC, c)

				if p == 0 {
					copyOfC[0] = (copyOfC[0] + 1) % (n + 1)
				} else {
					copyOfC[p] = copyOfC[p-1]
				}

				temp := nofStepsToSafeConf(copyOfC) + 1
				if temp > steps {
					steps = temp
				}
			}
		}

		nofSteps[string(c)] = steps
		return steps
	}
}

func simulate(ringSize byte) {
	n = ringSize
	configurations := getAllConfigurations()
	maxSteps := 0
	for _, c := range configurations {
		//if index%10000 == 0 {
		//	fmt.Println("index =", index)
		//}
		steps := nofStepsToSafeConf(c)
		if steps > maxSteps {
			maxSteps = steps
		}
	}
	fmt.Println("n =", n, "max =", maxSteps)
}

func main() {
	fmt.Print()
	for n := 3; n <= 7; n++ {
		simulate(byte(n))
	}
}
