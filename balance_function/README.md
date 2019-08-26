
We want to generate a balance function and find the amount of time it takes before the project will break even. A
polynomial function is created and the balance function should return the roots.

The balance function = cost function - revenue function
    A negative balance (one where costs outweigh revenue) is represented by a positive value in this model.

The cost function = overhead cost + recurring cost 
    The overhead cost is a function of assets (likely the number of LEVs chosen to be deployed). A simplified model can
    exclude the cost of any phase beyond phase I.
    
   The recurring cost, or upkeep, is a function of assets and time. However, the time should only be a simple 
   multiplier: (cost to maintain and operate n assets per annum) * number of years. A simplified model can also be
   created.
    
The revenue function = revenue prior to fusion technology + revenue after fusion technology
    Revenue prior to fusion technology models the revenue from a market where He-3 is sold to fusion and medical 
    research
    
    Revenue after fusion technology models the revenue from a market where He-3 can be converted into energy
    
    It is possible to modify the revenue after fusion technology model to also include a percentage of He-3 sold for
    research
    
    Revenue(assets) = Rev_before(assets) * (u(0) - u(t)) + (Rev_after(assets) (1 - P) + Rev_before(assets) (P)) * (u(t))
    Where u() is the heaviside function and P is the percentage of He-3 expected to go to research and development.


It may be worthwhile to generate the cost and revenue functions on a yearly basis, if the number of assets is expected
to change from year to year (more rocket launches sending more LEVs per year)
