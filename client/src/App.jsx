import { useState } from 'react'

import {
    Box,
    Heading,
    Text,
    Grid,
    VStack,
    Input,
    InputGroup,
    InputRightElement,
    Button,
    Code,
    Flex,
    Link
} from '@chakra-ui/react'
import { Icon } from '@chakra-ui/react'
import { FaGithub } from "react-icons/fa";

import AnswerBox from './components/AnswerBox'


function App() {
    const [query, setQuery] = useState('')
    const [answer, setAnswer] = useState('')


    async function handleClick() {
        const response = await fetch('http://127.0.0.1:7680/api/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ query: query })
        })
        const answer = await response.json()
        setAnswer(answer)
    }

    return (
        <Box minH={'100vh'}>
            <Box bg="gray.800" color="white" py={4}>
                <Flex alignItems="center" justifyContent="flex-end" px={8} pt={2}>
                    <Button display={{ base: "block", md: "none" }} onClick={() => console.log("menu clicked")}>
                        Menu
                    </Button>
                    <Box display={{ base: "none", md: "flex" }}>
                        <a
                            href='https://github.com/9akashnp8/team-bhp-riding-gear-assistant'
                            target="_blank">
                            <Icon as={FaGithub} boxSize={6} />
                        </a>
                    </Box>
                </Flex>
            </Box>
            <Grid
                placeContent={'center'}
                pt={14}
            >
                <VStack w={['80%', '80%', '80%', '60%']} m={'auto'}>
                    <Heading mb={3}>Riding Gear Assistant</Heading>
                    <Text fontSize='md' pb={3}>
                        <Code>gpt-3.5-turbo</Code> supercharged with the rich knowledge base of TBHP's Riding Gear thread.
                    </Text>
                    <InputGroup size='md'>
                        <Input
                            pr='4.5rem'
                            placeholder='Enter password'
                            onChange={(e) => setQuery(e.target.value)}
                        />
                        <InputRightElement width='5.5rem'>
                            <Button
                                h='1.8rem'
                                size='lg'
                                colorScheme='green'
                                onClick={handleClick}>
                                Ask
                            </Button>
                        </InputRightElement>
                    </InputGroup>
                    <p>
                        {answer
                            ? <AnswerBox answer={answer.response} />
                            : null}
                    </p>
                </VStack>
            </Grid>
        </Box>
    )
}

export default App
