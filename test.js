let data = ['Developer',
'Developer',
'Project Supervisor',
'Group Leader',
'Technical Lead',
'QA Specialist',
'QA Specialist',
'Director Of Online Development',
'Accountant',
'QA Specialist',
'Developer',
'QA Specialist',
'QA Specialist',
'Developer',
'Developer',
'Developer',
'Developer',
'QA Specialist',
'Animator/Developer',
'Developer',
'Developer',
'Office Admin',
'Developer',
'IT Security Engineer',
'Developer',
'Project Manager',
'Project Manager',
'Developer',
'Group Leader',
'Developer',
'Project Manager',
'Developer',
'Developer',
'Project Manager',
'Developer',
'Developer',
'QA Specialist',
'Technical Lead',
'Developer',
'Developer',
'Project Manager']

let uniqueArr = []
for (let item of data) {
    if (!uniqueArr.includes(item)) {
        uniqueArr.push(item)
    }
}
console.log(uniqueArr)