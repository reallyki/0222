{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04c360c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def input_stu(stu) :\n",
    "    stu['name'] = input('Name : ')\n",
    "    stu['age'] = input('Age : ')\n",
    "\n",
    "def output_stu(stu) :\n",
    "    print(student_)\n",
    "    print('이름 = %s, 나이 = %s입니다.' % (stu['name'], stu['age']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "541a341b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name : really\n",
      "Age : 25\n",
      "{'name': 'really', 'age': '25'}\n",
      "이름 = really, 나이 = 25입니다.\n"
     ]
    }
   ],
   "source": [
    "student_ = {}\n",
    "\n",
    "if __name__ == '__main__' :\n",
    "    input_stu(student_)\n",
    "    output_stu(student_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50af0c03",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
