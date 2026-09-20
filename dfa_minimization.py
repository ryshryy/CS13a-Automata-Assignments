print("DFA MINIMIZATION ASSIGNMENT")
print("Rachel Joy P. Pacot")
print("="*50)

def print_transition_table(states, alphabet, transitions, start_state, final_states, title):
    print(f"\n{'='*40}")
    print(f" {title} ")
    print(f"{'='*40}")
    print("Original Transition Table:")
    print("State\t|\t0\t|\t1")
    print("-" * 35)
    for state in states:
        marker = "->" if state == start_state else ("*" if state in final_states else "  ")
        if state == start_state and state in final_states: marker = "->*"

        t0 = transitions[state]['0']
        t1 = transitions[state]['1']
        print(f"{marker}{state}\t|\t{t0}\t|\t{t1}")
    print("-" * 35)

def minimize_dfa(states, alphabet, transitions, start_state, final_states):
    # Step 1: 0 Equivalence (Separate non-final and final states)
    f_set = set(final_states)
    nf_set = set(states) - f_set

    partitions = []
    if nf_set: partitions.append(sorted(list(nf_set)))
    if f_set: partitions.append(sorted(list(f_set)))

    equivs = [partitions]
    k = 0
    print(f"\n{k} EQUIVALENCE")
    print_partition(partitions)

    # Step 2: Loop to find 1, 2, 3... equivalences until minimized
    while True:
        prev_p = equivs[-1]
        new_p = []

        for group in prev_p:
            sub_groups = {}
            for state in group:
                # Get the signature of the state based on where it transitions to
                sig = []
                for symbol in alphabet:
                    dest = transitions[state][symbol]
                    for i, p in enumerate(prev_p):
                        if dest in p:
                            sig.append(i)
                            break
                sig = tuple(sig)

                if sig not in sub_groups:
                    sub_groups[sig] = []
                sub_groups[sig].append(state)

            for sg in sub_groups.values():
                new_p.append(sg)

        # Sort for clean output comparing
        new_p = sorted([sorted(g) for g in new_p])
        prev_p_sorted = sorted([sorted(g) for g in prev_p])

        k += 1
        print(f"{k} EQUIVALENCE")
        print_partition(new_p)

        if new_p == prev_p_sorted:
            print("Status: Minimized!")
            break

        equivs.append(new_p)

    # Step 3: Plot the new minimized transition table
    print("\nNew Minimized Transition Table:")
    print("State\t|\t0\t|\t1")
    print("-" * 35)

    minimized_states = []
    for group in new_p:
        name = "".join(group)
        minimized_states.append(name)

    for group in new_p:
        rep = group[0] # Take representative state from the group
        name = "".join(group)

        # Figure out new markers
        marker = "->" if any(s == start_state for s in group) else ("*" if any(s in final_states for s in group) else "  ")
        if any(s == start_state for s in group) and any(s in final_states for s in group): marker = "->*"

        # Find destinations for 0 and 1
        dest0_rep = transitions[rep]['0']
        dest1_rep = transitions[rep]['1']

        dest0_name = "".join(next(g for g in new_p if dest0_rep in g))
        dest1_name = "".join(next(g for g in new_p if dest1_rep in g))

        print(f"{marker}{name}\t|\t{dest0_name}\t|\t{dest1_name}")
    print("-" * 35)

def print_partition(partition):
    formatted = " ".join(["{" + ",".join(g) + "}" for g in partition])
    print(f"  {formatted}")


# ==========================================
# TEST CASES
# ==========================================
alphabet = ['0', '1']

# #1: Example ni Sir Josh 1
states_1 = ['A', 'B', 'C', 'D', 'E']
start_1 = 'A'
final_1 = ['E']
trans_1 = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'B', '1': 'D'},
    'C': {'0': 'B', '1': 'C'},
    'D': {'0': 'B', '1': 'E'},
    'E': {'0': 'B', '1': 'C'}
}
print_transition_table(states_1, alphabet, trans_1, start_1, final_1, "#1: Example ni Sir Josh 1")
minimize_dfa(states_1, alphabet, trans_1, start_1, final_1)


# #2: Example ni Sir Josh 2
states_2 = ['A', 'B', 'C', 'D', 'E', 'F']
start_2 = 'A'
final_2 = ['C', 'D', 'E']
trans_2 = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'A', '1': 'D'},
    'C': {'0': 'E', '1': 'F'},
    'D': {'0': 'E', '1': 'F'},
    'E': {'0': 'E', '1': 'F'},
    'F': {'0': 'F', '1': 'F'}
}
print_transition_table(states_2, alphabet, trans_2, start_2, final_2, "#2: Example ni Sir Josh 2")
minimize_dfa(states_2, alphabet, trans_2, start_2, final_2)


# #3: Own example 1
states_3 = ['A', 'B', 'C', 'D', 'E']
start_3 = 'A'
final_3 = ['E']
trans_3 = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'D', '1': 'E'},
    'C': {'0': 'D', '1': 'E'},  # B and C will merge
    'D': {'0': 'D', '1': 'D'},
    'E': {'0': 'E', '1': 'E'}
}
print_transition_table(states_3, alphabet, trans_3, start_3, final_3, "#3: Own example 1")
minimize_dfa(states_3, alphabet, trans_3, start_3, final_3)


# #4: Own example 2
states_4 = ['A', 'B', 'C', 'D', 'E', 'F']
start_4 = 'A'
final_4 = ['D', 'E']
trans_4 = {
    'A': {'0': 'B', '1': 'C'},
    'B': {'0': 'D', '1': 'F'},
    'C': {'0': 'E', '1': 'F'},
    'D': {'0': 'D', '1': 'D'},
    'E': {'0': 'D', '1': 'D'},  # D and E have same behavior and both are final
    'F': {'0': 'F', '1': 'F'}
}
print_transition_table(states_4, alphabet, trans_4, start_4, final_4, "#4: Own example 2")
minimize_dfa(states_4, alphabet, trans_4, start_4, final_4)
